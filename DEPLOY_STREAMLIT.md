# Deploy to Streamlit Cloud (FREE)

## Quick Start - 5 Minutes

### Step 1: Prepare Your Code
Run this script from your project folder:
```bash
deploy_to_streamlit.bat
```

This initializes git and prepares your code.

### Step 2: Create GitHub Account (FREE)
1. Go to https://github.com/signup
2. Sign up (takes 1 minute)
3. Verify your email

### Step 3: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `nist-scorer`
3. Click "Create repository"
4. Copy the commands shown

### Step 4: Push Your Code
Run these commands (replace `YOUR_USERNAME`):
```bash
git remote add origin https://github.com/YOUR_USERNAME/nist-scorer.git
git branch -M main
git push -u origin main
```

### Step 5: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Click "New app"
3. Select:
   - GitHub account (connect)
   - Repository: `YOUR_USERNAME/nist-scorer`
   - Branch: `main`
   - Main file path: `app.py`
4. Click "Deploy"

### Step 6: Get Your Link!
Streamlit will give you a public URL like:
```
https://nist-scorer.streamlit.app
```

**Share this link with your team!**

---

## What Users See

✅ Download example CSV from sidebar
✅ Edit with their school's data
✅ Upload to score compliance
✅ See dashboard instantly
✅ Download scored results

---

## Free Features

- ✅ Unlimited public apps
- ✅ Automatic updates (push to GitHub → auto-deploy)
- ✅ Custom domain support
- ✅ Community support
- ✅ No credit card needed

---

## Troubleshooting

**"Git not found"**
→ Install Git: https://git-scm.com/download/win

**"Authentication failed"**
→ Use GitHub personal access token:
1. Go to https://github.com/settings/tokens
2. Generate new token (check `repo`)
3. Use token as password when pushing

**"App won't load"**
→ Check requirements.txt has pandas and streamlit
→ Check app.py exists in root folder

---

## That's It!

Your compliance scorer is now live and free! 🎉
