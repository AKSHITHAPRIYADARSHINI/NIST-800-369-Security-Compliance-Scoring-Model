# Deployment Guide

## Option 1: Streamlit Cloud (Recommended - Easiest)

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign up with GitHub
3. Click "New app"
4. Select your repository: `NIST-800-369-Security-Compliance-Scoring-Model`
5. Select `main` branch and `app.py` as the main file
6. Click "Deploy"

Your app will be live in minutes at: `https://<username>-nist-compliance-scorer.streamlit.app`

---

## Option 2: Firebase Cloud Run Deployment

### Prerequisites
- Google Cloud Project with Firebase enabled
- `gcloud` CLI installed
- GitHub repository connected

### Step 1: Create Firebase Project
```bash
# Login to Google Cloud
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com containerregistry.googleapis.com
```

### Step 2: Deploy to Cloud Run
```bash
# Deploy from your local machine
gcloud run deploy nist-compliance-scorer \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

Your app will be available at the Cloud Run service URL.

### Step 3: Setup CI/CD with Cloud Build
1. Connect your GitHub repository to Cloud Build
2. Create a trigger pointing to your repository
3. Cloud Build will automatically deploy on every push to `main`

---

## Option 3: Manual Docker Deployment

```bash
# Build Docker image
docker build -t nist-compliance-scorer .

# Run locally
docker run -p 8501:8501 nist-compliance-scorer

# Push to Google Container Registry
docker tag nist-compliance-scorer gcr.io/YOUR_PROJECT_ID/nist-compliance-scorer
docker push gcr.io/YOUR_PROJECT_ID/nist-compliance-scorer

# Deploy to Cloud Run
gcloud run deploy nist-compliance-scorer \
  --image gcr.io/YOUR_PROJECT_ID/nist-compliance-scorer \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## Testing Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then visit: `http://localhost:8501`

---

## Features

✅ Upload NIST 800-369 compliance CSV files
✅ Calculate compliance scores automatically
✅ Download example CSV from sidebar
✅ View domain-level compliance metrics
✅ Filter and analyze controls
✅ Export scored results
