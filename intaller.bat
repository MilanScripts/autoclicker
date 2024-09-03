@echo off
echo ========================================
echo Installing Python Dependencies
echo ========================================
echo Waiting for 3 seconds downloading dependancys
timeout 3
python -m venv venv
call venv\Scripts\activate

echo Installing required Python packages...
pip install --upgrade pip
pip install -r requirements.txt

echo ========================================
echo Installation Complete
echo To activate the virtual environment, use:
echo call venv\Scripts\activate
echo ========================================

echo Waiting for 5 seconds before closing...
timeout /t 5

pause