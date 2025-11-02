# Ghost Pavilion Backend Deployment - Session History

**Date:** October 29, 2025
**Project:** Ghost Pavilion Website Backend Deployment to Railway
**Repository:** https://github.com/jahpe777/ghost_pavilion_2025

---

## Session Overview

This session focused on deploying the Django backend with PostgreSQL database to Railway hosting platform. The frontend was already deployed to Vercel at ghostpavilion.com.

---

## Initial State

- **Frontend:** React + Vite app deployed to Vercel at ghostpavilion.com
- **Backend:** Django 5.2 REST API with PostgreSQL running locally only
- **Features:** Email signup with SendGrid integration (info@ghostpavilion.com)
- **Issue:** Backend not deployed, so production signup form wouldn't work

---

## Deployment Process

### 1. Railway Setup

**Initial Configuration Files Created:**

#### `backend/requirements.txt`
```
asgiref==3.8.1
Django==5.2
django-cors-headers==4.7.0
djangorestframework==3.16.0
psycopg2-binary==2.9.10
sqlparse==0.5.3
gunicorn==23.0.0
sendgrid==6.12.0
dj-database-url==2.1.0
```

#### `backend/runtime.txt`
```
python-3.12.0
```

#### `backend/Procfile` (Final Version)
```
web: bash start.sh
```

#### `backend/start.sh` (Final Version)
```bash
#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting server..."
gunicorn ghostpavilion_backend.wsgi --bind 0.0.0.0:$PORT
```

### 2. Django Settings Configuration

**Updated `backend/ghostpavilion_backend/settings.py`:**

```python
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', "django-insecure-@e61b5qbw54+e3s28)&=yr$x2=(-*m(%34r99%-c*q!7)+f9a(")
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://jameshiggs:Theside!12345@localhost:5432/ghostpavilion_db',
        conn_max_age=600
    )
}

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://ghostpavilion.com",
    "https://www.ghostpavilion.com",
]

# SendGrid configuration
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
FROM_EMAIL = 'info@ghostpavilion.com'
```

### 3. Railway CLI Installation and Setup

```bash
# Install Railway CLI
brew install railway

# Login to Railway
railway login

# Initialize project
cd backend
railway init
# Selected: "James Higgs's Projects" workspace
# Project name: ghost-pavilion-backend

# Add PostgreSQL database
railway add --database postgres
```

### 4. Environment Variables Set

**Via Railway CLI:**
```bash
railway variables --set "SENDGRID_API_KEY=[YOUR_SENDGRID_KEY]"
railway variables --set "DJANGO_SECRET_KEY=[YOUR_DJANGO_SECRET]"
railway variables --set "ALLOWED_HOSTS=postgres-production-e00b.up.railway.app,ghostpavilion.com,www.ghostpavilion.com"
```

**Via Railway Web Dashboard (for ghost_pavilion_2025 service):**
- `DATABASE_URL` = Reference from Postgres service
- `SENDGRID_API_KEY` = (SendGrid API key)
- `DJANGO_SECRET_KEY` = (Django secret key)
- `ALLOWED_HOSTS` = (comma-separated domains)

### 5. Railway Service URL Generated

```bash
railway domain
# Generated: https://postgres-production-e00b.up.railway.app
```

---

## Issues Encountered and Solutions

### Issue 1: Vite Build Compatibility
**Problem:** react-favicon package incompatible with React 18
**Error:** `'Favicon' cannot be used as a JSX component`
**Solution:** Removed react-favicon, used standard `<link rel="icon">` in index.html

### Issue 2: Vercel Output Directory Mismatch
**Problem:** Vercel expected "dist" but Vite outputs to "build"
**Solution:** Created `frontend/vercel.json`:
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "installCommand": "npm install"
}
```

### Issue 3: Railway Deployment Target Confusion
**Problem:** Django app deployed to Postgres service instead of separate web service
**Root Cause:** Only one service existed, so `railway up` deployed to Postgres service
**Solution:** Created separate GitHub-connected service via Railway web dashboard:
- Service name: `ghost_pavilion_2025`
- Root Directory: `backend`
- Connected to GitHub repo: `jahpe777/ghost_pavilion_2025`

### Issue 4: Database Connection Refused (ONGOING)
**Problem:** Postgres service stuck running Django startup script instead of PostgreSQL
**Error:** `connection to server at "postgres.railway.internal" port 5432 failed: Connection refused`
**Status:** UNRESOLVED - Postgres service needs to be reset to run actual PostgreSQL database

---

## Railway Project Structure (Final State)

```
ghost-pavilion-backend (Railway Project)
├── Postgres (Service) - ISSUE: Running Django app instead of database
│   ├── postgres-production-e00b.up.railway.app
│   └── Volume: postgres-volume
└── ghost_pavilion_2025 (Service) - Django web app
    ├── Status: Crashed (can't connect to database)
    ├── Root Directory: backend
    └── Variables:
        ├── DATABASE_URL (reference to Postgres)
        ├── SENDGRID_API_KEY
        ├── DJANGO_SECRET_KEY
        └── ALLOWED_HOSTS
```

---

## Git Commit History

```
52f9d8f - Simplify startup script - remove database wait loop
14bafba - Add database wait logic to startup script
998cddf - Add startup script with migrations
df2f855 - Add automatic migrations to Procfile
fe08fb5 - Configure Django for Railway deployment
```

---

## Current Deployment Status

### ✅ Completed:
- Frontend deployed to Vercel (https://ghostpavilion.com)
- Railway project created with PostgreSQL
- Django settings configured for production
- Environment variables set
- Startup script with automatic migrations created
- Separate Django service created in Railway

### ❌ Blocking Issues:
1. **Postgres service corrupted:** Running Django startup script instead of PostgreSQL database
2. **Django service crashing:** Cannot connect to database because Postgres isn't running

### 🔧 Next Steps Required:
1. **Fix Postgres Service:**
   - Go to Postgres service → Settings
   - Remove custom Start Command (should be empty for default Postgres)
   - Redeploy Postgres service

2. **Verify Database Connection:**
   - Check Postgres service logs show actual PostgreSQL startup
   - Confirm `postgres.railway.internal:5432` is accepting connections

3. **Redeploy Django Service:**
   - Once Postgres is healthy, redeploy ghost_pavilion_2025 service
   - Verify migrations run successfully
   - Generate public domain for Django API

4. **Update Frontend:**
   - Update frontend API endpoint to point to Railway backend URL
   - Test email signup flow end-to-end

---

## Key URLs

- **Frontend:** https://ghostpavilion.com (Vercel)
- **Backend (intended):** TBD - needs Railway domain generation
- **GitHub Repository:** https://github.com/jahpe777/ghost_pavilion_2025
- **Railway Project:** https://railway.com/project/fc1c8f74-16d6-458d-8093-7154c443f48a
- **SendGrid Sender:** info@ghostpavilion.com

---

## Important Credentials & Configuration

### SendGrid
- **API Key:** `[STORED IN RAILWAY VARIABLES]`
- **Sender Email:** info@ghostpavilion.com
- **Purpose:** Welcome emails for new subscribers

### Django Secret Key
```
[STORED IN RAILWAY VARIABLES]
```

### Local PostgreSQL (Development)
- **Database:** ghostpavilion_db
- **User:** jameshiggs
- **Password:** [STORED LOCALLY]
- **Host:** localhost
- **Port:** 5432

### Railway PostgreSQL (Production)
- **Database:** railway
- **User:** postgres
- **Password:** [STORED IN RAILWAY VARIABLES]
- **Internal Host:** postgres.railway.internal:5432
- **Public Host:** gondola.proxy.rlwy.net:45442
- **Connection String:** `[STORED IN RAILWAY VARIABLES AS DATABASE_URL]`

---

## File Structure (Backend)

```
backend/
├── ghostpavilion_backend/
│   ├── __init__.py
│   ├── settings.py          # Updated for Railway
│   ├── urls.py
│   └── wsgi.py
├── mailing/
│   ├── models.py            # Email subscriber model
│   ├── views.py             # SignUpCreateView with SendGrid
│   ├── management/
│   │   └── commands/
│   │       └── send_mass_email.py
│   └── ...
├── manage.py
├── requirements.txt         # Production dependencies
├── runtime.txt              # Python 3.12.0
├── Procfile                 # Railway web process definition
├── start.sh                 # Startup script with migrations
└── sendgrid.env             # Local env file (NOT in git)
```

---

## Django Apps & Features

### Mailing App
- **Purpose:** Email signup and newsletter management
- **Model:** Subscriber (email field)
- **API Endpoint:** `/api/signup/`
- **Features:**
  - Email validation
  - Duplicate prevention
  - SendGrid welcome email on signup
  - Mass email management command

**Welcome Email Template:** Professional HTML email with Ghost Pavilion branding

---

## Commands Reference

### Local Development
```bash
# Activate virtual environment
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

# Install dependencies
pip install -r backend/requirements.txt

# Run migrations
python backend/manage.py migrate

# Run development server
python backend/manage.py runserver

# Send mass email
python backend/manage.py send_mass_email "Subject" "Message"
```

### Railway Deployment
```bash
# Login
railway login

# Link to project
railway link

# Set service
railway service ghost_pavilion_2025

# View logs
railway logs

# Check variables
railway variables

# Deploy
railway up

# Generate public domain
railway domain
```

### Git Commands Used
```bash
git add .
git commit -m "message"
git push origin master
```

---

## Frontend Integration (TODO)

Once backend is deployed and has a public URL, update frontend to call:

```javascript
// frontend/src/SignUpPage/SignUpPage.tsx
const API_URL = 'https://[RAILWAY_DOMAIN]/api/signup/';

// Change from:
// const API_URL = 'http://localhost:8000/api/signup/';
```

Test signup flow:
1. Visit ghostpavilion.com
2. Enter email in signup form
3. Verify email saved to Railway PostgreSQL
4. Check welcome email delivered via SendGrid

---

## Pending Tasks (From Todo List)

1. ⏳ **Deploy Django backend to Railway with PostgreSQL** (IN PROGRESS - blocked)
2. ⏸️ **Create first Meta ad campaign without verification**
3. ⏸️ **Verify SendGrid sender authentication is complete**
4. ⏸️ **Start creating first AI music video for next release**

---

## Session Notes

- User experienced frustration with Railway's complexity compared to expectations
- Multiple circular issues with Railway CLI service selection
- Key learning: Railway separates database and web services, but CLI doesn't make this obvious
- Resolution required using web dashboard to create proper service separation
- Final blocker: Accidentally deployed Django app TO the Postgres service, corrupting it

---

## For New Laptop Setup

1. Clone repository:
```bash
git clone https://github.com/jahpe777/ghost_pavilion_2025.git
cd ghost_pavilion_2025
```

2. Create Python virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

3. Install backend dependencies:
```bash
pip install -r backend/requirements.txt
```

4. Create `backend/sendgrid.env`:
```bash
export SENDGRID_API_KEY='[YOUR_SENDGRID_API_KEY]'
```

5. Set up local PostgreSQL database:
```bash
createdb ghostpavilion_db
```

6. Run migrations:
```bash
python backend/manage.py migrate
```

7. Install frontend dependencies:
```bash
cd frontend
npm install
```

---

## End of Session Summary

**Duration:** ~2 hours
**Outcome:** Partially successful - configuration complete but deployment blocked
**Deliverables:**
- ✅ All code committed and pushed to GitHub
- ✅ Railway project created with services
- ✅ Configuration files created
- ❌ Backend not yet accessible (Postgres service needs fix)

**Recommended Next Session:**
1. Fix Postgres service in Railway dashboard
2. Complete Django deployment
3. Test end-to-end email signup
4. Move on to Meta ad campaign creation
