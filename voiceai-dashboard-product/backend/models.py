"""Database models for VoiceAI Call Analysis"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CallImport(Base):
    """Track CSV import sessions"""
    __tablename__ = "call_imports"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String, nullable=False)
    total_calls = Column(Integer, default=0)
    status = Column(String, default="pending")  # pending, processing, completed, failed
    analysis_date = Column(DateTime, nullable=True)
    excel_report_path = Column(String, nullable=True)
    error_message = Column(Text, nullable=True)
    
    # Relationship
    call_records = relationship("CallRecord", back_populates="import")
    analysis_log = relationship("AnalysisLog", back_populates="import", uselist=False)


class CallRecord(Base):
    """Individual call data"""
    __tablename__ = "call_records"
    
    id = Column(Integer, primary_key=True, index=True)
    import_id = Column(Integer, ForeignKey("call_imports.id"), nullable=False)
    
    # Call metadata
    call_id = Column(String, nullable=False, index=True)
    call_date = Column(DateTime, nullable=True, index=True)
    duration_seconds = Column(Integer, nullable=True)
    
    # Issue & Resolution
    issue_category = Column(String, nullable=True, index=True)
    resolution_status = Column(String, nullable=True)
    
    # Sentiment & Satisfaction
    sentiment = Column(String, nullable=True, index=True)  # Positive, Neutral, Negative
    csat_score = Column(Float, nullable=True)
    
    # Additional info
    bot_effectiveness = Column(String, nullable=True)
    transfer_reason = Column(String, nullable=True)
    friction_points = Column(Text, nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    import_ = relationship("CallImport", back_populates="call_records")


class DailyMetric(Base):
    """Pre-aggregated daily metrics for performance"""
    __tablename__ = "daily_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False, unique=True, index=True)
    
    # Volume metrics
    total_calls = Column(Integer, default=0)
    negative_sentiment_count = Column(Integer, default=0)
    positive_sentiment_count = Column(Integer, default=0)
    neutral_sentiment_count = Column(Integer, default=0)
    
    # Satisfaction metrics
    avg_csat = Column(Float, nullable=True)
    satisfied_count = Column(Integer, default=0)  # 4-5 stars
    dissatisfied_count = Column(Integer, default=0)  # 1-2 stars
    
    # Resolution metrics
    resolved_count = Column(Integer, default=0)
    escalated_count = Column(Integer, default=0)
    abandoned_count = Column(Integer, default=0)
    
    # Issue breakdown (JSON for flexibility)
    top_issues = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TrendData(Base):
    """Time-series aggregations for trend analysis"""
    __tablename__ = "trend_data"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False, index=True)
    period = Column(String, nullable=False)  # daily, weekly, monthly
    
    # Percentages
    negative_sentiment_pct = Column(Float, nullable=True)
    positive_sentiment_pct = Column(Float, nullable=True)
    resolution_rate_pct = Column(Float, nullable=True)
    
    # Aggregates
    total_calls = Column(Integer, default=0)
    avg_csat = Column(Float, nullable=True)
    avg_duration = Column(Integer, nullable=True)
    
    # Change metrics (for DoD, WoW, MoM)
    sentiment_change = Column(Float, nullable=True)  # % point change
    csat_change = Column(Float, nullable=True)
    resolution_change = Column(Float, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)


class AnalysisLog(Base):
    """Track skill analysis executions"""
    __tablename__ = "analysis_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    import_id = Column(Integer, ForeignKey("call_imports.id"), nullable=False)
    
    # Skill execution
    skill_name = Column(String, default="voiceai_call_analysis")
    execution_time_ms = Column(Integer, nullable=True)
    tokens_used = Column(Integer, nullable=True)
    status = Column(String, nullable=False)  # success, failed
    error_message = Column(Text, nullable=True)
    
    # Results
    analysis_results = Column(JSON, nullable=True)
    
    executed_at = Column(DateTime, default=datetime.utcnow)
    
    import_ = relationship("CallImport", back_populates="analysis_log")
