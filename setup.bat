@echo off
:: Setup script for ZeroCode LLM Chat Client
echo Setting up ZeroCode LLM Chat Client...

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Error: Python is not installed or not in PATH. Please install Python 3.8 or higher.
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo Please edit the .env file and add your API keys.
)

echo.
echo Setup complete! You can now run the application with:
echo start.bat
echo.
echo Don't forget to edit the .env file to add your API keys if you haven't already.
