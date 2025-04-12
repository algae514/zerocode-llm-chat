#!/usr/bin/env python
"""
Run script for the ZeroCode LLM Chat Client
This script launches the Streamlit app
"""
import os
import subprocess
import sys
from dotenv import load_dotenv

def main():
    """Main entry point for the run script"""
    # Load environment variables
    load_dotenv()
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please set it in your .env file or environment")
        return 1
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Run the Streamlit app
    print("Starting ZeroCode LLM Chat Client...")
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", os.path.join(script_dir, "src", "main.py")],
            check=True
        )
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nApplication terminated by user")
        return 0

if __name__ == "__main__":
    sys.exit(main())
