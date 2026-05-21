# VoiceAI Call Analysis Dashboard

A production-ready web application for analyzing voice AI bot and call center data with real-time sentiment analysis, trend tracking, and interactive visualizations.

## 🎯 Features

✅ **Data Upload**
- Drag-and-drop CSV file upload
- Automatic data validation
- Real-time processing with voiceai_call_analysis skill
- Upload history tracking

✅ **Analytics Dashboard**
- KPI cards (total calls, sentiment %, CSAT, resolution rate)
- Real-time metrics calculation
- Interactive charts (7+ chart types)
- Drill-down capabilities

✅ **Trend Analysis**
- Day-over-Day (DoD) comparisons
- Week-over-Week (WoW) trends
- Month-over-Month (MoM) growth
- Custom date range analysis
- Sentiment trend visualization

✅ **Interactive Filters**
- Date range picker
- Sentiment filter (Positive/Neutral/Negative)
- CSAT score bins (1-2, 3, 4-5)
- Issue category filtering
- Real-time data refresh

✅ **Data Export**
- Excel report generation
- Multiple sheet formats
- Call-level detail export
- Ready for dashboard ingestion

✅ **Scalability**
- Prepared for automated daily/weekly data ingestion
- Multi-brand support ready
- Alerting hooks available
- Performance optimized

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Or: Node.js 18+, Python 3.10+, PostgreSQL 13+

### Option 1: Docker (Recommended)

```bash
# Clone/extract the project
cd voiceai-dashboard-product

# Start all services
docker-compose up -d

# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Local Setup

**Backend Setup:**
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your database URL

# Create database
# (PostgreSQL must be running)

# Start backend
python -m uvicorn main:app --reload
```

**Frontend Setup:**
```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

## 📊 Dashboard Overview

### 1. Upload Tab
- Drag-drop CSV files with call data
- Automatic skill invocation
- Real-time processing status
- Import history

### 2. Dashboard Tab
- **KPI Cards**: Total calls, negative sentiment %, CSAT, resolution rate
- **Sentiment Distribution**: Pie chart breakdown
- **Top Issues**: Bar chart by negative sentiment
- **Trend Analysis**: Line chart sentiment over time
- **Issue Breakdown**: Detailed table by category

### 3. Data Tab (Coming Soon)
- Raw call data explorer
- Advanced filtering
- Export to Excel
- Download individual records

## 🔧 API Endpoints

### Upload & Analysis
```
POST   /api/upload          - Upload CSV file
POST   /api/analyze         - Trigger skill analysis
GET    /api/status/{id}     - Check analysis status
```

### Data Queries
```
GET    /api/metrics         - Get KPI summary
GET    /api/data            - Get paginated call records
GET    /api/issues          - Get issue breakdown
GET    /api/sentiment       - Get sentiment trends
GET    /api/csat            - Get CSAT analysis
GET    /api/history         - Get import history
```

### Export & Admin
```
POST   /api/export/excel    - Generate Excel report
DELETE /api/import/{id}     - Delete import
GET    /health              - Health check
```

## 📁 Project Structure

```
voiceai-dashboard-product/
├── backend/                    # FastAPI application
│   ├── main.py                # Main API app
│   ├── models.py              # SQLAlchemy ORM models
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example           # Environment template
│   └── Dockerfile             # Backend container
│
├── frontend/                   # React application
│   ├── src/
│   │   ├── App.tsx            # Main component
│   │   ├── main.tsx           # React entry point
│   │   ├── store.ts           # Zustand state management
│   │   ├── api.ts             # API client
│   │   ├── index.css          # Tailwind styles
│   │   └── components/
│   │       ├── Dashboard.tsx   # Main dashboard
│   │       ├── Upload.tsx      # File upload
│   │       └── Filters.tsx     # Filter controls
│   ├── package.json           # NPM dependencies
│   ├── vite.config.ts         # Vite config
│   ├── tailwind.config.js     # Tailwind CSS
│   ├── index.html             # HTML entry
│   └── Dockerfile             # Frontend container
│
├── docker-compose.yml          # Multi-container setup
├── ARCHITECTURE.md             # System design
└── README.md                   # This file
```

## 🗄️ Database Schema

### Tables
- **call_imports**: Track upload sessions
- **call_records**: Individual call data (indexed by sentiment, date, issue)
- **daily_metrics**: Pre-aggregated daily statistics
- **trend_data**: Time-series aggregations
- **analysis_logs**: Skill execution records

## 🔌 Integration with voiceai_call_analysis

The dashboard automatically:
1. Detects uploaded CSV format
2. Invokes voiceai_call_analysis skill
3. Stores analyzed data
4. Generates trend metrics
5. Exports Excel reports

Skills path configured in `.env` (backend).

## 📈 CSV File Format

Expected columns:
```
call_id, date, duration, issue_category, resolution_status, 
sentiment, csat, bot_effectiveness, transfer_reason, friction_points
```

See `backend/models.py` for complete field mapping.

## 🔐 Security

- Input validation on all endpoints
- CSV schema validation
- Rate limiting (ready to add)
- CORS configured
- Environment-based secrets
- Database connection pooling

## 📊 Metrics Explained

- **Negative Sentiment %**: Percentage of calls with negative sentiment
- **CSAT**: Customer Satisfaction Average (1-5 scale)
- **Resolution Rate**: % of calls marked as resolved
- **Satisfaction Rate**: % of calls with CSAT ≥ 4

## 🚀 Future Enhancements

1. **Automation**
   - Scheduled daily/weekly data ingestion
   - Email reports
   - Webhook integrations

2. **Advanced Analytics**
   - Anomaly detection
   - Predictive trends
   - Customer cohort analysis
   - Root cause analysis

3. **Alerts & Notifications**
   - Slack integration
   - Email alerts
   - Threshold-based notifications
   - Anomaly detection

4. **Multi-Tenancy**
   - Support multiple brands/teams
   - Role-based access control
   - Data isolation

5. **Mobile & Real-time**
   - React Native mobile app
   - WebSocket live updates
   - Mobile-optimized dashboard

6. **Integrations**
   - Salesforce CRM sync
   - Zendesk integration
   - Google Sheets export
   - Power BI connector

## 🛠️ Troubleshooting

### Backend Connection Error
```bash
# Check if PostgreSQL is running
docker-compose ps

# Check backend logs
docker-compose logs backend
```

### Frontend Not Loading
```bash
# Check if API is accessible
curl http://localhost:8000/health

# Check frontend logs
docker-compose logs frontend
```

### Database Issues
```bash
# Reset database
docker-compose down -v
docker-compose up -d
```

## 📞 Support

For issues or questions about:
- **voiceai_call_analysis skill**: See skill documentation
- **Dashboard UI**: Check frontend components in `frontend/src`
- **API**: See `ARCHITECTURE.md` for endpoint details

## 📄 License

Built with voiceai_call_analysis skill

## 🎯 Next Steps

1. **Deploy**: Use docker-compose for production
2. **Connect Data**: Set up automated CSV feeds
3. **Customize**: Modify Filters, Charts per your needs
4. **Integrate**: Connect to your existing tools
5. **Monitor**: Set up alerts for key metrics

---

**Ready to analyze your voice AI performance? Let's go\! 🚀**
