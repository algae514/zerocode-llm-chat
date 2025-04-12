#!/bin/bash

# Setup script for ZeroCode LLM Chat Client
echo "Setting up ZeroCode LLM Chat Client..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit the .env file and add your API keys."
fi

echo ""
echo "Setup complete! You can now run the application with:"
echo "./start.sh"
echo ""
echo "Don't forget to edit the .env file to add your API keys if you haven't already."
