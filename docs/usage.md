# ZeroCode LLM Chat Client - Usage Guide

## Getting Started

### Prerequisites

- Python 3.8 or higher
- API keys for at least one LLM provider:
  - OpenAI API key for GPT models
  - Anthropic API key for Claude models

### Installation

1. Clone the repository and navigate to the project directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   ```bash
   cp .env.example .env
   ```
5. Edit the `.env` file and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ANTHROPIC_API_KEY=your_anthropic_key_here
   ```

### Running the Application

To start the application, run:

```bash
./start.sh  # On Windows: start.bat
```

Or use:

```bash
streamlit run src/main.py
```

This will launch the Streamlit application and open it in your default web browser.

## Features

### Chat Interface

The chat interface is built using Streamlit and provides:

- Text input for user messages
- Display of conversation history
- Provider and model selection in the sidebar
- Temperature and max token controls
- Option to clear conversation history

### LLM Integration

The application supports integration with:

- OpenAI GPT models
  - gpt-3.5-turbo
  - gpt-4
- Anthropic Claude models
  - claude-3-opus (maps to claude-3-opus-20240229)
  - claude-3-sonnet (maps to claude-3-sonnet-20240229)
  - claude-3-haiku (maps to claude-3-haiku-20240307)

## API Keys

### OpenAI API Key

To get an OpenAI API key:
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API keys section
4. Create a new secret key
5. Add this key to your .env file as `OPENAI_API_KEY=your_key_here`

### Anthropic API Key

To get an Anthropic API key:
1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to the API Keys section
4. Create a new API key
5. Add this key to your .env file as `ANTHROPIC_API_KEY=your_key_here`

## Troubleshooting

### API Key Issues

If you encounter errors related to API keys:

1. Check that your `.env` file contains the correct API key
2. Verify that the key has not expired
3. Ensure you have sufficient credits/quota with your LLM provider

### Model Not Found Errors

If you see "model not found" errors:

1. Make sure you're using a valid model name
2. The application handles mapping friendly model names to their full API versions
3. The model versions may change over time, check the provider's documentation

### Connection Problems

If the application cannot connect to the LLM API:

1. Check your internet connection
2. Verify the API endpoint is correct
3. Check if the service is experiencing downtime

## Contributing

Contributions to improve the application are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.
