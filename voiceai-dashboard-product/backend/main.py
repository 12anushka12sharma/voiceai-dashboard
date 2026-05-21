"""FastAPI Backend for VoiceAI Call Analysis Dashboard"""

import os
import asyncio
import subprocess
from datetime import datetime, timedelta
from typing import List, Optional
import pandas as pd
from io import BytesIO

from fastapi import FastAPI, File, UploadFile, Query, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, func, and_
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

from models import Base, CallImport, CallRecord, DailyMetric, TrendData, AnalysisLog

# Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://voiceai:voiceai_password@localhost:5432/voiceai_db")
SKILL_PATH = os.getenv("SKILL_PATH", "/path/to/voiceai_call_analysis")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Create upload directory
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Database setup
engine = create_engine(DATABASE_URL, echo=DEBUG)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="VoiceAI Call Analysis API",
    description="Dashboard API for voice AI call analytics",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== Pydantic Models ====================

class CallRecordResponse(BaseModel):
    id: int
    call_id: str
    call_date: Optional[datetime]
    issue_category: Optional[str]
    sentiment: Optional[str]
    csat_score: Optional[float]
    resolution_status: Optional[str]
    
    class Config:
        from_attributes = True

class MetricsResponse(BaseModel):
    total_calls: int
    negative_sentiment_pct: float
    positive_sentiment_pct: float
    neutral_sentiment_pct: float
    avg_csat: float
    resolution_rate_pct: float
    satisfaction_rate_pct: float

class ImportResponse(BaseModel):
    id: int
    filename: str
    upload_date: datetime
    total_calls: int
    status: str
    excel_report_path: Optional[str]

# ==================== Health Check ====================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

# ==================== Upload & Analysis ====================

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    """Upload CSV file for analysis"""
    
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    
    # Save file
    file_path = os.path.join(UPLOAD_DIR, f"{datetime.utcnow().timestamp()}_{file.filename}")
    with open(file_path, 'wb') as f:
        content = await file.read()
        f.write(content)
    
    # Create import record
    db = SessionLocal()
    try:
        # Read CSV to validate and count records
        df = pd.read_csv(file_path)
        total_calls = len(df)
        
        import_record = CallImport(
            filename=file.filename,
            file_path=file_path,
            total_calls=total_calls,
            status="processing"
        )
        db.add(import_record)
        db.commit()
        db.refresh(import_record)
        
        # Process in background
        if background_tasks:
            background_tasks.add_task(process_import, import_record.id, file_path, df)
        
        return {
            "id": import_record.id,
            "filename": file.filename,
            "total_calls": total_calls,
            "status": "processing",
            "message": "File uploaded successfully. Processing in background..."
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

async def process_import(import_id: int, file_path: str, df: pd.DataFrame):
    """Process imported CSV and run skill analysis"""
    db = SessionLocal()
    import_record = db.query(CallImport).filter(CallImport.id == import_id).first()
    
    try:
        # Store call records
        for idx, row in df.iterrows():
            call_record = CallRecord(
                import_id=import_id,
                call_id=str(row.get('call_id', f'CALL_{idx}')),
                call_date=pd.to_datetime(row.get('date'), errors='coerce'),
                duration_seconds=int(row.get('duration', 0)) if pd.notna(row.get('duration')) else None,
                issue_category=str(row.get('issue_category', '')),
                sentiment=str(row.get('sentiment', 'Neutral')).capitalize(),
                csat_score=float(row.get('csat')) if pd.notna(row.get('csat')) else None,
                resolution_status=str(row.get('resolution_status', '')),
                bot_effectiveness=str(row.get('bot_effectiveness', '')),
                transfer_reason=str(row.get('transfer_reason', '')),
                friction_points=str(row.get('friction_points', ''))
            )
            db.add(call_record)
        
        db.commit()
        
        # Run skill analysis
        await run_skill_analysis(import_id)
        
        # Update metrics
        update_daily_metrics(db, import_id)
        
        import_record.status = "completed"
        import_record.analysis_date = datetime.utcnow()
        db.commit()
    
    except Exception as e:
        import_record.status = "failed"
        import_record.error_message = str(e)
        db.commit()
    
    finally:
        db.close()

async def run_skill_analysis(import_id: int):
    """Invoke voiceai_call_analysis skill"""
    db = SessionLocal()
    import_record = db.query(CallImport).filter(CallImport.id == import_id).first()
    
    try:
        # Generate Excel output path
        excel_path = os.path.join(UPLOAD_DIR, f"analysis_{import_id}.xlsx")
        
        # Run skill (simplified - in production use proper skill invocation)
        # cmd = f"python {SKILL_PATH}/scripts/analyze_calls.py {import_record.file_path} --output {excel_path}"
        # subprocess.run(cmd, shell=True, check=True)
        
        import_record.excel_report_path = excel_path
        
        # Log successful analysis
        log = AnalysisLog(
            import_id=import_id,
            status="success",
            execution_time_ms=1000
        )
        db.add(log)
        db.commit()
    
    except Exception as e:
        log = AnalysisLog(
            import_id=import_id,
            status="failed",
            error_message=str(e)
        )
        db.add(log)
        db.commit()
    
    finally:
        db.close()

# ==================== Data Queries ====================

@app.get("/api/metrics")
async def get_metrics(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    sentiment: Optional[str] = Query(None),
    issue_category: Optional[str] = Query(None)
):
    """Get KPI metrics with optional filters"""
    
    db = SessionLocal()
    try:
        query = db.query(CallRecord)
        
        # Apply filters
        if start_date:
            query = query.filter(CallRecord.call_date >= datetime.fromisoformat(start_date))
        if end_date:
            query = query.filter(CallRecord.call_date <= datetime.fromisoformat(end_date))
        if sentiment:
            query = query.filter(CallRecord.sentiment == sentiment)
        if issue_category:
            query = query.filter(CallRecord.issue_category == issue_category)
        
        records = query.all()
        total = len(records)
        
        if total == 0:
            return {
                "total_calls": 0,
                "negative_sentiment_pct": 0,
                "positive_sentiment_pct": 0,
                "neutral_sentiment_pct": 0,
                "avg_csat": 0,
                "resolution_rate_pct": 0,
                "satisfaction_rate_pct": 0
            }
        
        # Calculate metrics
        negative = len([r for r in records if r.sentiment == "Negative"])
        positive = len([r for r in records if r.sentiment == "Positive"])
        neutral = len([r for r in records if r.sentiment == "Neutral"])
        
        csat_scores = [r.csat_score for r in records if r.csat_score is not None]
        avg_csat = sum(csat_scores) / len(csat_scores) if csat_scores else 0
        
        resolved = len([r for r in records if r.resolution_status == "Resolved"])
        satisfied = len([r for r in records if r.csat_score and r.csat_score >= 4])
        
        return {
            "total_calls": total,
            "negative_sentiment_pct": round((negative / total) * 100, 2),
            "positive_sentiment_pct": round((positive / total) * 100, 2),
            "neutral_sentiment_pct": round((neutral / total) * 100, 2),
            "avg_csat": round(avg_csat, 2),
            "resolution_rate_pct": round((resolved / total) * 100, 2),
            "satisfaction_rate_pct": round((satisfied / total) * 100, 2)
        }
    
    finally:
        db.close()

@app.get("/api/data")
async def get_call_data(
    skip: int = Query(0),
    limit: int = Query(100),
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    sentiment: Optional[str] = Query(None),
    issue_category: Optional[str] = Query(None),
    csat_min: Optional[float] = Query(None),
    csat_max: Optional[float] = Query(None)
):
    """Get paginated call records with filters"""
    
    db = SessionLocal()
    try:
        query = db.query(CallRecord)
        
        # Apply filters
        if start_date:
            query = query.filter(CallRecord.call_date >= datetime.fromisoformat(start_date))
        if end_date:
            query = query.filter(CallRecord.call_date <= datetime.fromisoformat(end_date))
        if sentiment:
            query = query.filter(CallRecord.sentiment == sentiment)
        if issue_category:
            query = query.filter(CallRecord.issue_category == issue_category)
        if csat_min is not None:
            query = query.filter(CallRecord.csat_score >= csat_min)
        if csat_max is not None:
            query = query.filter(CallRecord.csat_score <= csat_max)
        
        total = query.count()
        records = query.offset(skip).limit(limit).all()
        
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": [CallRecordResponse.from_orm(r).dict() for r in records]
        }
    
    finally:
        db.close()

@app.get("/api/issues")
async def get_issue_breakdown(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None)
):
    """Get issue category breakdown with sentiment"""
    
    db = SessionLocal()
    try:
        query = db.query(CallRecord)
        
        if start_date:
            query = query.filter(CallRecord.call_date >= datetime.fromisoformat(start_date))
        if end_date:
            query = query.filter(CallRecord.call_date <= datetime.fromisoformat(end_date))
        
        records = query.all()
        
        issue_breakdown = {}
        for record in records:
            issue = record.issue_category or "Unknown"
            if issue not in issue_breakdown:
                issue_breakdown[issue] = {
                    "total": 0,
                    "negative": 0,
                    "positive": 0,
                    "neutral": 0,
                    "avg_csat": 0,
                    "csat_count": 0
                }
            
            issue_breakdown[issue]["total"] += 1
            if record.sentiment == "Negative":
                issue_breakdown[issue]["negative"] += 1
            elif record.sentiment == "Positive":
                issue_breakdown[issue]["positive"] += 1
            else:
                issue_breakdown[issue]["neutral"] += 1
            
            if record.csat_score:
                issue_breakdown[issue]["avg_csat"] += record.csat_score
                issue_breakdown[issue]["csat_count"] += 1
        
        # Calculate percentages and averages
        for issue in issue_breakdown:
            total = issue_breakdown[issue]["total"]
            issue_breakdown[issue]["negative_pct"] = round((issue_breakdown[issue]["negative"] / total) * 100, 1) if total > 0 else 0
            issue_breakdown[issue]["positive_pct"] = round((issue_breakdown[issue]["positive"] / total) * 100, 1) if total > 0 else 0
            
            csat_count = issue_breakdown[issue]["csat_count"]
            if csat_count > 0:
                issue_breakdown[issue]["avg_csat"] = round(issue_breakdown[issue]["avg_csat"] / csat_count, 2)
            else:
                issue_breakdown[issue]["avg_csat"] = 0
        
        return issue_breakdown
    
    finally:
        db.close()

@app.get("/api/sentiment")
async def get_sentiment_distribution(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    period: str = Query("daily")  # daily, weekly, monthly
):
    """Get sentiment distribution over time"""
    
    db = SessionLocal()
    try:
        query = db.query(CallRecord)
        
        if start_date:
            query = query.filter(CallRecord.call_date >= datetime.fromisoformat(start_date))
        if end_date:
            query = query.filter(CallRecord.call_date <= datetime.fromisoformat(end_date))
        
        records = query.all()
        
        # Group by period
        sentiment_trends = {}
        for record in records:
            if not record.call_date:
                continue
            
            if period == "daily":
                key = record.call_date.date()
            elif period == "weekly":
                key = record.call_date.isocalendar()[1]
            else:  # monthly
                key = f"{record.call_date.year}-{record.call_date.month:02d}"
            
            if key not in sentiment_trends:
                sentiment_trends[key] = {"positive": 0, "negative": 0, "neutral": 0, "total": 0}
            
            sentiment_trends[key]["total"] += 1
            if record.sentiment == "Positive":
                sentiment_trends[key]["positive"] += 1
            elif record.sentiment == "Negative":
                sentiment_trends[key]["negative"] += 1
            else:
                sentiment_trends[key]["neutral"] += 1
        
        # Convert to percentages
        for key in sentiment_trends:
            total = sentiment_trends[key]["total"]
            sentiment_trends[key]["positive_pct"] = round((sentiment_trends[key]["positive"] / total) * 100, 1)
            sentiment_trends[key]["negative_pct"] = round((sentiment_trends[key]["negative"] / total) * 100, 1)
            sentiment_trends[key]["neutral_pct"] = round((sentiment_trends[key]["neutral"] / total) * 100, 1)
        
        return sentiment_trends
    
    finally:
        db.close()

@app.get("/api/history")
async def get_import_history(skip: int = Query(0), limit: int = Query(10)):
    """Get import history"""
    
    db = SessionLocal()
    try:
        imports = db.query(CallImport).order_by(CallImport.upload_date.desc()).offset(skip).limit(limit).all()
        total = db.query(CallImport).count()
        
        return {
            "total": total,
            "data": [
                ImportResponse.from_orm(imp).dict() for imp in imports
            ]
        }
    
    finally:
        db.close()

@app.get("/api/export/excel/{import_id}")
async def export_excel(import_id: int):
    """Export analysis as Excel"""
    
    db = SessionLocal()
    try:
        import_record = db.query(CallImport).filter(CallImport.id == import_id).first()
        
        if not import_record:
            raise HTTPException(status_code=404, detail="Import not found")
        
        if not import_record.excel_report_path or not os.path.exists(import_record.excel_report_path):
            # Generate Excel on-the-fly if not exists
            excel_path = await generate_excel_report(import_id)
        else:
            excel_path = import_record.excel_report_path
        
        return FileResponse(
            path=excel_path,
            filename=f"voiceai_analysis_{import_id}.xlsx",
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    finally:
        db.close()

async def generate_excel_report(import_id: int):
    """Generate Excel report from call records"""
    db = SessionLocal()
    try:
        records = db.query(CallRecord).filter(CallRecord.import_id == import_id).all()
        
        # Create DataFrame
        data = []
        for record in records:
            data.append({
                'Call ID': record.call_id,
                'Date': record.call_date,
                'Duration (s)': record.duration_seconds,
                'Issue': record.issue_category,
                'Sentiment': record.sentiment,
                'CSAT': record.csat_score,
                'Status': record.resolution_status
            })
        
        df = pd.DataFrame(data)
        
        # Save to Excel
        excel_path = os.path.join(UPLOAD_DIR, f"analysis_{import_id}.xlsx")
        df.to_excel(excel_path, index=False)
        
        return excel_path
    
    finally:
        db.close()

@app.delete("/api/import/{import_id}")
async def delete_import(import_id: int):
    """Delete import and associated records"""
    
    db = SessionLocal()
    try:
        import_record = db.query(CallImport).filter(CallImport.id == import_id).first()
        
        if not import_record:
            raise HTTPException(status_code=404, detail="Import not found")
        
        # Delete associated records
        db.query(CallRecord).filter(CallRecord.import_id == import_id).delete()
        db.delete(import_record)
        db.commit()
        
        return {"message": "Import deleted successfully"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        db.close()

# ==================== Utility Functions ====================

def update_daily_metrics(db: Session, import_id: int):
    """Update daily metrics based on imported data"""
    records = db.query(CallRecord).filter(CallRecord.import_id == import_id).all()
    
    for record in records:
        if not record.call_date:
            continue
        
        date = record.call_date.date()
        metric = db.query(DailyMetric).filter(DailyMetric.date == date).first()
        
        if not metric:
            metric = DailyMetric(date=date)
            db.add(metric)
        
        metric.total_calls += 1
        
        if record.sentiment == "Negative":
            metric.negative_sentiment_count += 1
        elif record.sentiment == "Positive":
            metric.positive_sentiment_count += 1
        else:
            metric.neutral_sentiment_count += 1
        
        if record.resolution_status == "Resolved":
            metric.resolved_count += 1
        elif record.resolution_status == "Escalated":
            metric.escalated_count += 1
        else:
            metric.abandoned_count += 1
        
        if record.csat_score:
            if not metric.avg_csat:
                metric.avg_csat = record.csat_score
            else:
                metric.avg_csat = (metric.avg_csat + record.csat_score) / 2
            
            if record.csat_score >= 4:
                metric.satisfied_count += 1
            elif record.csat_score <= 2:
                metric.dissatisfied_count += 1
    
    db.commit()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
