#!/bin/bash

# Start script for ZeroCode LLM Chat Client
echo "Starting ZeroCode LLM Chat Client..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run setup.sh first."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found. Please run setup.sh first."
    exit 1
fi

# Run the application
echo "Launching application..."
python -m streamlit run src/main.py

# Deactivate virtual environment on exit
deactivate
