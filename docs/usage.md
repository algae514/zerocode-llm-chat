# ZeroCode LLM Chat Client - Usage Guide

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (or other supported LLM provider API keys)

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
5. Edit the `.env` file and add your API keys

### Running the Application

To start the application, run:

```bash
streamlit run src/main.py
```

This will launch the Streamlit application and open it in your default web browser.

## Features

### Chat Interface

The chat interface is built using Streamlit and provides:

- Text input for user messages
- Display of conversation history
- Model selection in the sidebar
- Option to clear conversation history

### LLM Integration

The application supports integration with:

- OpenAI GPT models (default)
- Future support for additional LLM providers

## Customization

### Changing Default Models

You can modify the available models by editing the `chat_interface.py` file:

```python
model = st.selectbox(
    "Select Model",
    ["gpt-3.5-turbo", "gpt-4", "claude-3-opus", "claude-3-sonnet"]
)
```

### Adding New Features

To extend the application, you can:

1. Add new LLM providers in the `llm` module
2. Enhance the UI in the `ui` module
3. Add additional settings and configurations

## Troubleshooting

### API Key Issues

If you encounter errors related to API keys:

1. Check that your `.env` file contains the correct API key
2. Verify that the key has not expired
3. Ensure you have sufficient credits/quota with your LLM provider

### Connection Problems

If the application cannot connect to the LLM API:

1. Check your internet connection
2. Verify the API endpoint is correct
3. Check if the service is experiencing downtime

## Contributing

Contributions to improve the application are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.
