# ZeroCode LLM Chat Client

A Python-based application that works as a chat client with Large Language Models, supporting both OpenAI and Anthropic models.

## Features

- Interactive chat interface using Streamlit
- Support for multiple LLM providers:
  - OpenAI GPT models
  - Anthropic Claude models
- Model selection and configuration
- Conversation history management
- Temperature and response length controls

## Installation

```bash
# Clone the repository
git clone https://github.com/algae514/zerocode-llm-chat.git
cd zerocode-llm-chat

# Using setup scripts
# For Linux/macOS:
./setup.sh

# For Windows:
setup.bat
```

Or manually:

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Using start scripts
# For Linux/macOS:
./start.sh

# For Windows:
start.bat
```

Or manually:

```bash
# Set up your environment variables
cp .env.example .env
# Edit .env file with your API keys

# Run the application
streamlit run src/main.py
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```
# OpenAI API Key (for GPT models)
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic API Key (for Claude models)
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

You need at least one of these API keys to use the application.

## Supported Models

### OpenAI Models
- gpt-3.5-turbo
- gpt-4

### Anthropic Claude Models
- claude-3-opus (maps to claude-3-opus-20240229)
- claude-3-sonnet (maps to claude-3-sonnet-20240229)
- claude-3-haiku (maps to claude-3-haiku-20240307)

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
├── setup.sh           # Setup script for Linux/macOS
├── setup.bat          # Setup script for Windows
├── start.sh           # Start script for Linux/macOS
├── start.bat          # Start script for Windows
└── README.md          # Project documentation
```

## More Information

See the `docs/usage.md` file for detailed usage instructions and troubleshooting.

## License

[MIT License](LICENSE)
