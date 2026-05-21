# VoiceAI Call Analysis Product - Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    React Frontend                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ - File Upload (Drag & Drop)                         │   │
│  │ - Dashboard with KPI Cards                          │   │
│  │ - Interactive Charts (Recharts)                     │   │
│  │ - Advanced Filters & Exploration                    │   │
│  │ - Trend Analysis (DoD, Weekly, Monthly)             │   │
│  │ - Excel Export                                      │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/REST
┌────────────────────▼────────────────────────────────────────┐
│                 FastAPI Backend                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ API Endpoints:                                      │   │
│  │ - POST /api/upload - Handle CSV file uploads       │   │
│  │ - POST /api/analyze - Invoke voiceai skill         │   │
│  │ - GET /api/data - Query aggregated data            │   │
│  │ - GET /api/trends - Time-series data               │   │
│  │ - GET /api/metrics - KPI calculations              │   │
│  │ - POST /api/export - Generate Excel reports        │   │
│  │ - GET /api/history - Import history                │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
    ┌────────┐  ┌──────────┐  ┌────────┐
    │ Skill  │  │PostgreSQL│  │ File   │
    │ Runner │  │ Database │  │Storage │
    └────────┘  └──────────┘  └────────┘
```

## Database Schema

### Tables:
1. **call_imports** - Track upload sessions
2. **call_records** - All individual call data
3. **daily_metrics** - Pre-aggregated daily stats
4. **trend_data** - Time-series aggregations
5. **analysis_logs** - Skill execution logs

## Key Features

### 1. Data Import
- Drag-drop CSV upload
- Automatic data validation
- Skill invocation on upload
- Data deduplication

### 2. Analytics Dashboard
- Real-time metrics
- 7+ interactive chart types
- Multi-level drill-down
- Side-by-side comparisons

### 3. Trend Analysis
- Day-over-Day (DoD) changes
- Week-over-Week (WoW) trends
- Month-over-Month (MoM) growth
- Custom date range analysis

### 4. Interactive Filters
- Date range picker
- Sentiment filter (Positive/Neutral/Negative)
- Issue category multi-select
- CSAT score bins (1-2, 3, 4-5)
- Resolution status filter
- Custom filter combinations

### 5. Data Export
- Excel workbook generation
- Multiple sheet formats
- Chart-ready data
- Scheduled exports (future)

## Tech Stack

**Frontend:**
- React 18 + TypeScript
- Vite (fast bundling)
- Tailwind CSS (styling)
- Recharts (visualizations)
- Axios (HTTP client)
- Zustand (state management)

**Backend:**
- Python 3.10+
- FastAPI (async API framework)
- SQLAlchemy (ORM)
- Pydantic (validation)
- Python subprocess (skill invocation)
- pandas (data processing)
- openpyxl (Excel generation)

**Database:**
- PostgreSQL 13+
- Alembic (migrations)

**DevOps:**
- Docker & Docker Compose
- Environment-based config

## API Design

```
BASE_URL: http://localhost:8000/api

UPLOAD & ANALYSIS:
POST   /upload          - Upload CSV file
POST   /analyze         - Trigger skill on data
GET    /status/{id}     - Check analysis status

DATA QUERIES:
GET    /data            - Get filtered call records
GET    /metrics         - Get KPI summary
GET    /trends          - Get time-series data
GET    /issues          - Get issue breakdown
GET    /sentiment       - Get sentiment distribution
GET    /csat            - Get CSAT analysis

COMPARISONS:
GET    /compare/dod     - Day-over-day
GET    /compare/wow     - Week-over-week
GET    /compare/mom     - Month-over-month

EXPORT:
POST   /export/excel    - Generate Excel report
GET    /history         - Import history

ADMIN:
GET    /health          - Health check
DELETE /data/{id}       - Delete import
```

## Data Flow

1. **User uploads CSV** → Frontend validates → POST /api/upload
2. **Backend processes** → Validates schema → Stores in PostgreSQL
3. **Skill invocation** → Runs voiceai_call_analysis → Gets Excel + analysis
4. **Data aggregation** → Calculates metrics → Updates trend tables
5. **Dashboard refresh** → Frontend polls → Displays updated data
6. **Export** → User requests → Generate Excel → Download

## Deployment

### Local Development:
```bash
docker-compose up -d
npm run dev        # Frontend
python -m uvicorn main:app --reload  # Backend
```

### Production:
- Container orchestration (Kubernetes/ECS)
- PostgreSQL managed service
- Static file CDN
- API load balancer

## Security Considerations

- Input validation on all endpoints
- CSV schema validation
- Rate limiting on uploads
- Data isolation per user (future: multi-tenancy)
- Encrypted database connections
- CORS configuration

## Future Enhancements

1. **Automation** - Scheduled daily/weekly data ingestion
2. **Alerts** - Anomaly detection, threshold alerts
3. **ML Insights** - Predictive analytics, clustering
4. **Multi-tenancy** - Support multiple brands/teams
5. **Real-time** - WebSocket updates
6. **Mobile** - React Native companion app
7. **Integrations** - Slack, email reports
