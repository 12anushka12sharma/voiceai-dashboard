# VoiceAI Dashboard Setup Guide

Complete step-by-step instructions for setting up the VoiceAI Call Analysis Dashboard.

## ✅ Prerequisites

### Required
- Docker & Docker Compose (for easiest setup)
- OR: PostgreSQL 13+, Python 3.10+, Node.js 18+
- voiceai_call_analysis skill installed/available

### System Requirements
- 2GB+ RAM
- 500MB+ disk space
- Modern browser (Chrome, Firefox, Safari, Edge)

## 🐳 Installation Method 1: Docker (Recommended)

### Step 1: Prepare the Project

```bash
# Navigate to project directory
cd voiceai-dashboard-product

# Verify structure
ls -la
# Should show: backend/, frontend/, docker-compose.yml, README.md, ARCHITECTURE.md
```

### Step 2: Configure Environment

```bash
# Backend configuration
cd backend
cp .env.example .env

# (Edit .env if needed - defaults work out of the box)
cd ..
```

### Step 3: Start Services

```bash
# Start all services (database, backend, frontend)
docker-compose up -d

# Wait 10 seconds for database to initialize
sleep 10

# Check status
docker-compose ps
```

Expected output:
```
voiceai_postgres   running
voiceai_backend    running
voiceai_frontend   running
```

### Step 4: Access the Dashboard

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

### Step 5: Verify Everything Works

```bash
# Check backend health
curl http://localhost:8000/health

# Should return:
# {"status":"healthy","timestamp":"...","version":"1.0.0"}
```

### Step 6: Test File Upload

1. Go to http://localhost:5173
2. Click "📤 Upload Data" tab
3. Drag & drop a CSV file or select one
4. File should process and appear in "Recent Imports"

## 💻 Installation Method 2: Local Development

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create Python virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# OR on Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Edit .env with your database connection
# Example for local PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost:5432/voiceai_db

# Start backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend should be running at http://localhost:8000

### Frontend Setup

```bash
# In new terminal, navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend should be running at http://localhost:5173

### Database Setup

```bash
# Create PostgreSQL database (if not using Docker)
psql -U postgres

# Run these commands:
CREATE DATABASE voiceai_db;
CREATE USER voiceai WITH PASSWORD 'voiceai_password';
ALTER ROLE voiceai SET client_encoding TO 'utf8';
ALTER ROLE voiceai SET default_transaction_isolation TO 'read committed';
ALTER ROLE voiceai SET default_transaction_deferrable TO on;
ALTER ROLE voiceai SET default_transaction_read_only TO off;
GRANT ALL PRIVILEGES ON DATABASE voiceai_db TO voiceai;
```

## 📋 CSV File Format

Your call data CSV should have these columns:

```
call_id, date, duration, issue_category, resolution_status, 
sentiment, csat, bot_effectiveness, transfer_reason, friction_points
```

Example:
```csv
call_id,date,duration,issue_category,resolution_status,sentiment,csat,bot_effectiveness,transfer_reason,friction_points
CALL_001,2024-05-21,120,Shipping Delay,Escalated,Negative,2,Low,High Complexity,Customer frustrated with delivery date
CALL_002,2024-05-21,95,Account Issue,Resolved,Positive,5,High,,Successfully resolved
```

## 🔧 Configuration

### Environment Variables

**Backend (.env)**
```
DATABASE_URL=postgresql://voiceai:voiceai_password@localhost:5432/voiceai_db
DEBUG=True
HOST=0.0.0.0
PORT=8000
SKILL_PATH=/path/to/voiceai_call_analysis
UPLOAD_DIR=./uploads
```

**Frontend (Vite)**
- Automatically configured in `vite.config.ts`
- API proxied to http://localhost:8000

## 🧪 Testing the Setup

### Test 1: API Health

```bash
curl -X GET http://localhost:8000/health
```

Should return `{"status":"healthy",...}`

### Test 2: File Upload

```bash
# Create sample CSV
cat > sample.csv << EOF
call_id,date,duration,issue_category,resolution_status,sentiment,csat
CALL_001,2024-05-21,120,Shipping,Escalated,Negative,2
CALL_002,2024-05-21,95,Account,Resolved,Positive,5
