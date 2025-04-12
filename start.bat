@echo off
:: Start script for ZeroCode LLM Chat Client
echo Starting ZeroCode LLM Chat Client...

:: Check if virtual environment exists
if not exist venv (
    echo Virtual environment not found. Please run setup.bat first.
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Check if .env file exists
if not exist .env (
    echo Error: .env file not found. Please run setup.bat first.
    exit /b 1
)

:: Run the application
echo Launching application...
python -m streamlit run src\main.py

:: Deactivate virtual environment on exit
deactivate
