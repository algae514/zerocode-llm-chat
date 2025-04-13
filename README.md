# ZeroCode LLM Chat Client

A Python-based desktop application that works as a chat client with Large Language Models. ZeroCode provides a clean interface for conversing with AI models from OpenAI and Anthropic, with persistent conversation storage.

![ZeroCode LLM Chat](https://via.placeholder.com/800x450.png?text=ZeroCode+LLM+Chat+Client)

## Key Features

- **Multiple AI Providers** - Support for both OpenAI GPT models and Anthropic Claude models
- **Persistent Conversations** - All chats are automatically saved to a local SQLite database
- **Conversation Management** - Create, rename, switch between, and delete conversations
- **Import/Export** - Share conversations with others or back them up as JSON files
- **Clean UI** - Simple, intuitive interface built with Streamlit
- **Customizable Settings** - Adjust temperature, response length, and other parameters
- **Electron Ready** - Built to be packaged as a desktop application with Electron

## Quick Start

### Prerequisites

- Python 3.8 or higher
- An API key for OpenAI, Anthropic, or both

### Installation

```bash
# Clone the repository
git clone https://github.com/algae514/zerocode-llm-chat.git
cd zerocode-llm-chat

# Run the setup script
# For macOS/Linux:
./setup.sh

# For Windows:
setup.bat
```

### Configuration

1. Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

2. You need at least one of these API keys to use the application.

### Running

```bash
# For macOS/Linux:
./start.sh

# For Windows:
start.bat
```

## Detailed Documentation

For more complete information, see:
- [Usage Guide](docs/usage.md) - Detailed instructions for using the application
- [API Keys Guide](docs/api_keys.md) - How to obtain and configure API keys
- [Developer Guide](docs/developer.md) - Information for developers who want to extend the application

## Supported Models

### OpenAI Models
- gpt-3.5-turbo - Fast, cost-effective model for most use cases
- gpt-4 - More capable model for complex tasks

### Anthropic Claude Models
- claude-3-opus - Anthropic's most powerful model
- claude-3-sonnet - Balanced model for most use cases
- claude-3-haiku - Fast, efficient model for simpler tasks

## Conversation Storage

All conversations are automatically saved locally at:
- `~/.zerocode-llm-chat/chat_history.db` (on macOS/Linux)
- `C:\Users\YourUsername\.zerocode-llm-chat\chat_history.db` (on Windows)

## Privacy & Security

- All conversations are stored only on your local machine
- API keys are stored locally in your `.env` file
- No data is sent to any servers except the AI provider you choose (OpenAI or Anthropic)

## Future Plans

- Additional AI providers
- Conversation search
- Local model support
- Customizable themes
- Desktop applications for all platforms

## License

[MIT License](LICENSE)
