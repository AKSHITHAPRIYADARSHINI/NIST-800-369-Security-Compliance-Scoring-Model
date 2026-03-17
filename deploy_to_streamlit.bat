@echo off
REM NIST 800-369 Compliance Scorer - Deploy to Streamlit Cloud

echo.
echo ====================================================
echo   NIST 800-369 Compliance Scorer
echo   Streamlit Cloud Deployment Setup
echo ====================================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please download and install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✓ Git is installed
echo.

REM Initialize git
echo Initializing git repository...
git init
if errorlevel 1 goto error

echo Adding files...
git add .
if errorlevel 1 goto error

echo Creating initial commit...
git config user.email "nist-scorer@local.dev"
git config user.name "NIST Scorer"
git commit -m "NIST 800-369 Compliance Scorer - Ready for Streamlit Cloud"
if errorlevel 1 goto error

echo.
echo ====================================================
echo   NEXT STEPS
echo ====================================================
echo.
echo 1. Create a GitHub account (if you don't have one):
echo    https://github.com/signup
echo.
echo 2. Create a new repository on GitHub called:
echo    "nist-scorer" (or any name you prefer)
echo.
echo 3. Run these commands (replace YOUR_USERNAME):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/nist-scorer.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 4. Go to: https://share.streamlit.io
echo.
echo 5. Click "New app" and connect your GitHub repo
echo.
echo 6. Get your live link! (share.streamlit.io/YOUR_USERNAME/nist-scorer)
echo.
echo ====================================================
echo.
pause
exit /b 0

:error
echo.
echo ERROR: Something went wrong!
echo Please check your git installation or file permissions.
pause
exit /b 1
