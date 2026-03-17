@echo off
echo 📦 Installing dependencies...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to install dependencies. Make sure Python/pip is installed and on your PATH.
    pause
    exit /b
)

echo 🤖 Starting Welcome Bot...
python main.py
pause
