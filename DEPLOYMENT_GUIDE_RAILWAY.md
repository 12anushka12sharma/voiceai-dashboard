# Deploy VoiceAI Dashboard to Railway.app (FREE)

## Why Railway?
✅ $5/month free credits (covers your 5K-10K calls/day)
✅ PostgreSQL included
✅ Easy one-click deployment
✅ Auto-scaling for traffic spikes
✅ No credit card required initially
✅ Perfect for 5K-10K calls/day scale

---

## 🚀 Step-by-Step Deployment

### Step 1: Create Railway Account (2 minutes)

1. Go to **https://railway.app**
2. Click "Start Free"
3. Sign up with GitHub (easiest) or email
4. Verify email
5. You're in\! ✅

---

### Step 2: Prepare Your GitHub Repository (5 minutes)

You need to push your code to GitHub for Railway to deploy from.

```bash
# Initialize git repo (if not already done)
cd voiceai-dashboard-product
git init

# Add all files
git add .

# Commit
git commit -m "Initial VoiceAI Dashboard deployment"

# Create GitHub repo at github.com/new
# Call it: voiceai-dashboard
# Copy the repository URL

# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/voiceai-dashboard.git
git branch -M main
git push -u origin main
```

---

### Step 3: Deploy Backend to Railway (5 minutes)

1. **Log in to Railway**: https://railway.app/dashboard

2. **Click "New Project"**

3. **Select "Deploy from GitHub"**

4. **Connect GitHub & select your repo**
   - Click "Connect GitHub Account"
   - Authorize Railway
   - Select `voiceai-dashboard` repo

5. **Railway auto-detects it's a monorepo**
   - It will see `backend/` and `frontend/` folders

6. **Create Backend Service**
   - Click "Add Service" → "GitHub Repo"
   - Select the same repo
   - Set `Root Directory` to `backend/`
   - Name it: `voiceai-backend`

7. **Configure Environment**
   - Click on the service
   - Go to "Variables"
   - Add these:
   ```
   DATABASE_URL=postgresql://[AUTO-FILLED BY RAILWAY]
   DEBUG=False
   PORT=8000
   SKILL_PATH=/path/to/voiceai_call_analysis
   UPLOAD_DIR=/tmp/uploads
   PYTHONUNBUFFERED=1
   ```

8. **Add PostgreSQL**
   - In Railway dashboard, click "New Service"
   - Select "Database" → "PostgreSQL"
   - Select version 15
   - Railway auto-populates `DATABASE_URL` ✅

9. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - You'll see "Build successful" ✅

10. **Get Backend URL**
    - Click the backend service
    - Copy the public URL (looks like `https://voiceai-backend-prod.railway.app`)

---

### Step 4: Deploy Frontend to Railway (5 minutes)

1. **Create Frontend Service**
   - Click "New Service" → "GitHub Repo"
   - Same repo
   - Set `Root Directory` to `frontend/`
   - Name it: `voiceai-frontend`

2. **Configure Build**
   - Go to "Settings"
   - Set these environment variables:
   ```
   VITE_API_URL=https://voiceai-backend-prod.railway.app
   NODE_ENV=production
   ```

3. **Configure Start Command**
   - In "Deploy" settings
   - Start Command: `npm run build && npm run preview`
   - Or use Railway's default (it auto-detects)

4. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - You'll see "Build successful" ✅

5. **Get Frontend URL**
   - Click the frontend service
   - Copy the public URL (looks like `https://voiceai-frontend-prod.railway.app`)

---

## ✅ Verify Deployment

### Check Backend

```bash
curl https://voiceai-backend-prod.railway.app/health

# Should return:
# {"status":"healthy","timestamp":"...","version":"1.0.0"}
```

### Check Frontend

Open in browser:
```
https://voiceai-frontend-prod.railway.app
```

Should load the dashboard\! 🎉

---

## 📊 Testing Your Deployment

1. **Go to your frontend URL**
2. **Click "Upload Data" tab**
3. **Create a test CSV** or download sample from docs
4. **Upload the file**
5. **Check "Dashboard" tab**
6. **See charts populate** 📊

---

## 🔧 Environment Variables Reference

### Backend (.env variables in Railway)

| Variable | Value | Notes |
|----------|-------|-------|
| `DATABASE_URL` | Auto-filled by Railway | PostgreSQL connection |
| `DEBUG` | `False` | Production mode |
| `PORT` | `8000` | Railway default |
| `SKILL_PATH` | `/path/to/skill` | Optional, for automation |
| `UPLOAD_DIR` | `/tmp/uploads` | Temporary file storage |
| `PYTHONUNBUFFERED` | `1` | Better logging |

### Frontend (Vite environment)

| Variable | Value | Notes |
|----------|-------|-------|
| `VITE_API_URL` | Backend URL | Points to your Railway backend |
| `NODE_ENV` | `production` | Production build |

---

## 💰 Cost Breakdown (Monthly)

With 5K-10K calls/day:

| Service | Cost | Notes |
|---------|------|-------|
| Backend (Node) | ~$3 | Small instance |
| Frontend (Node) | ~$1 | Static files |
| PostgreSQL | ~$1 | Small database |
| **Total** | **~$5** | Covered by free credits\! |

---

## 🔒 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong database password (Railway generates one)
- [ ] Enable database backups (Railway includes daily backups)
- [ ] Monitor cost/usage (Railway dashboard)
- [ ] Set up alerts for high usage (Railway settings)

---

## 📈 Scaling as You Grow

### If you exceed free tier:
1. Link a credit card
2. Pay as you go (~$0.50/instance/hour)
3. For 5K-10K calls, costs stay ~$5-10/month

### For higher scale (later):
- Add caching layer (Redis)
- Database read replicas
- Auto-scaling groups
- CDN for frontend

---

## 🆘 Troubleshooting

### Backend not deploying?

```bash
# Check logs in Railway
# Go to Service → Logs tab
# Look for Python errors

# Common issues:
# 1. Missing requirements.txt - ✓ You have it
# 2. Python version mismatch - ✓ Should auto-detect
# 3. Database not connected - Check DATABASE_URL variable
```

### Frontend not loading?

```bash
# Check build logs
# Go to Service → Logs tab
# Look for npm errors

# Common issues:
# 1. Missing package.json - ✓ You have it
# 2. VITE_API_URL wrong - Double-check backend URL
# 3. Build timeout - Increase timeout in Railway settings
```

### Can't upload files?

```bash
# Backend issue likely
# Check:
# 1. /tmp/uploads directory permissions
# 2. Backend logs for errors
# 3. UPLOAD_DIR environment variable

# Solution: Use in-memory storage or Railway's ephemeral storage
```

---

## 🚀 Next Steps After Deployment

### 1. Verify Everything Works (Now)
- [ ] Backend health check passes
- [ ] Frontend loads
- [ ] Can upload CSV
- [ ] Charts populate

### 2. Set Up Monitoring (Today)
- [ ] Enable Railway alerts
- [ ] Monitor disk usage
- [ ] Watch API response times
- [ ] Check database size

### 3. Automate Data Feeds (This Week)
- [ ] Set up API endpoint for CSV uploads
- [ ] Create Python script for daily imports
- [ ] Schedule with cron or Railway workflows
- [ ] Test with sample data

### 4. Add Features (Next Week)
- [ ] Set up Slack alerts for high negative sentiment
- [ ] Add email reports
- [ ] Create custom dashboards
- [ ] Add user authentication

---

## 📞 Helpful Links

- **Railway Dashboard**: https://railway.app/dashboard
- **Railway Docs**: https://docs.railway.app
- **Backend Logs**: Your service → Logs
- **Network Tab**: Your service → Networking
- **Usage**: Account → Billing → Usage

---

## 🎉 That's It\!

Your VoiceAI Dashboard is live and accessible globally\! 🚀

**Your URLs:**
- Frontend: `https://voiceai-frontend-prod.railway.app`
- Backend: `https://voiceai-backend-prod.railway.app`
- API Docs: `https://voiceai-backend-prod.railway.app/docs`

---

## 💡 Pro Tips

### Tip 1: Rolling Deployments
- Railway automatically deploys on GitHub push
- Just commit and push, Railway redeploys automatically

### Tip 2: Environment Variables
- Use Railway's UI to manage secrets
- Never commit `.env` file
- Railway encrypts all variables

### Tip 3: Database Backups
- Railway auto-backs up PostgreSQL daily
- Accessible from service settings
- 7-day retention in free tier

### Tip 4: Custom Domain (Optional Later)
- Upgrade from `railway.app` subdomain
- Add your own domain in Railway settings
- Auto SSL certificate

---

**Ready to go live? Deploy now and start analyzing\! 🎊**
