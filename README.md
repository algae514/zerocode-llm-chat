# ZeroCode LLM Chat Client

A Python-based application that works as a chat client with Large Language Models.

## Features

- Interactive chat interface
- Support for various LLM providers
- Simple and clean UI

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd zerocode

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Set up your environment variables
cp .env.example .env
# Edit .env file with your API keys

# Run the application
python -m src.main
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```
OPENAI_API_KEY=your_openai_api_key_here
# Add other API keys as needed
```

## Project Structure

```
zerocode/
├── docs/              # Documentation
├── src/               # Source code
│   ├── __init__.py
│   ├── llm/           # LLM integration modules
│   ├── ui/            # UI components
│   └── main.py        # Entry point
├── tests/             # Test files
├── .env               # Environment variables (not in git)
├── .env.example       # Example environment file
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

## License

[MIT License](LICENSE)
