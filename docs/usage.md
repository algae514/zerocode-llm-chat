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

### Conversation Management

The application includes full conversation management features:

- Persistent storage of conversations using SQLite
- Create, view, and delete conversations
- Rename conversations
- Export conversations to JSON files
- Import conversations from JSON files

All conversations are automatically saved to a SQLite database in the user's home directory at:
- `~/.zerocode-llm-chat/chat_history.db` (on Linux/macOS)
- `C:\Users\YourUsername\.zerocode-llm-chat\chat_history.db` (on Windows)

### LLM Integration

The application supports integration with:

- OpenAI GPT models
  - gpt-3.5-turbo
  - gpt-4
- Anthropic Claude models
  - claude-3-opus (maps to claude-3-opus-20240229)
  - claude-3-sonnet (maps to claude-3-sonnet-20240229)
  - claude-3-haiku (maps to claude-3-haiku-20240307)

## Using the Interface

### Conversation Management

- **Create New Conversations**: Click the "New Conversation" button in the sidebar
- **Switch Between Conversations**: Click on a conversation title in the sidebar
- **Rename Conversations**: Edit the "Conversation Title" text field at the top of the chat
- **Delete Conversations**: Click the trash icon next to a conversation in the sidebar
- **Export Conversations**: Click "Export Current Conversation" to save a JSON file
- **Import Conversations**: Use the file uploader in the sidebar to import a previously exported conversation

### Chat Settings

All settings are available in the "Settings" expander:

1. **Provider Selection**: Choose between OpenAI and Anthropic
2. **Model Selection**: Select a specific model from the chosen provider
3. **Temperature**: Adjust the randomness of the responses (0.0 to 1.0)
4. **Max Response Length**: Set the maximum number of tokens for each response
5. **Clear Chat History**: Reset the current conversation while keeping its title

### API Keys

The application checks for API keys at startup. You'll see status indicators in the Settings panel:
- Green: The API key is configured
- Red: The API key is missing or invalid

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

### Database Issues

If you encounter issues with the conversation database:

1. The database file is located at `~/.zerocode-llm-chat/chat_history.db`
2. You can delete this file to reset all conversations (they will be permanently lost)
3. If the file becomes corrupted, the application will attempt to create a new one

### Model Not Found Errors

If you see "model not found" errors:

1. Make sure you're using a valid model name
2. The application handles mapping friendly model names to their full API versions
3. The model versions may change over time, check the provider's documentation

### Exported Conversations

Exported conversations are saved as JSON files with the following structure:
```json
{
  "conversation": {
    "id": "unique-id",
    "title": "Conversation Title",
    "model": "model-name",
    "created_at": "timestamp",
    "updated_at": "timestamp",
    "summary": "First message summary..."
  },
  "messages": [
    {
      "id": 1,
      "conversation_id": "unique-id",
      "role": "user",
      "content": "User message",
      "timestamp": "timestamp"
    },
    {
      "id": 2,
      "conversation_id": "unique-id",
      "role": "assistant",
      "content": "Assistant response",
      "timestamp": "timestamp"
    }
  ]
}
```

These files can be imported into any instance of the application.

## Electron Integration

This application is designed to be compatible with Electron for desktop deployment:

1. The SQLite database uses a local file storage model
2. All dependencies are compatible with Electron
3. The UI is responsive and adapts to different window sizes

When packaging as an Electron app:
- Ensure that API keys are securely stored
- Update the database path to use the Electron app's data directory
- Consider adding auto-update functionality

## Contributing

Contributions to improve the application are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.
