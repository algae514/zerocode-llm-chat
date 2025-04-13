# ZeroCode LLM Chat Client - Usage Guide

This guide provides detailed instructions for using the ZeroCode LLM Chat Client.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Getting Started](#getting-started)
- [Interface Overview](#interface-overview)
- [Conversation Management](#conversation-management)
- [Model Settings](#model-settings)
- [Import & Export](#import-and-export)
- [Troubleshooting](#troubleshooting)
- [Electron Usage](#electron-usage)

## Installation

### Prerequisites

- Python 3.8 or higher
- API keys for at least one LLM provider:
  - OpenAI API key for GPT models
  - Anthropic API key for Claude models

### Installation Steps

#### Using Setup Scripts (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/algae514/zerocode-llm-chat.git
   cd zerocode-llm-chat
   ```

2. Run the setup script:
   - On macOS/Linux:
     ```bash
     ./setup.sh
     ```
   - On Windows:
     ```bash
     setup.bat
     ```

This will:
- Create a virtual environment
- Install all dependencies
- Create a template .env file for your API keys

#### Manual Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/algae514/zerocode-llm-chat.git
   cd zerocode-llm-chat
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a .env file:
   ```bash
   cp .env.example .env
   ```

6. Edit the .env file to add your API keys.

## Configuration

### API Keys

You'll need at least one of the following API keys:

#### OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to "API Keys" in your account settings
4. Create a new secret key
5. Add to your .env file:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ```

#### Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to "API Keys"
4. Create a new API key
5. Add to your .env file:
   ```
   ANTHROPIC_API_KEY=your_anthropic_key_here
   ```

## Getting Started

### Launching the Application

Run the application using the start script:

- On macOS/Linux:
  ```bash
  ./start.sh
  ```
- On Windows:
  ```bash
  start.bat
  ```

Or manually:
```bash
streamlit run src/main.py
```

This will open the application in your default web browser.

## Interface Overview

The ZeroCode interface consists of:

### Sidebar (Left)
- Conversation list
- New conversation button
- Import/Export functions
- Show/Hide toggle

### Main Chat Area (Right)
- Conversation title (editable)
- Settings expander
- Chat history
- Message input field

## Conversation Management

### Creating a New Conversation

1. Click the "New Conversation" button in the sidebar
2. Start typing in the message input field
3. Your messages and the AI's responses will be saved automatically

### Switching Between Conversations

Click on any conversation title in the sidebar to load it.

### Renaming a Conversation

1. Edit the "Conversation Title" text field at the top of the main area
2. Press Enter to save the new title

### Deleting a Conversation

Click the trash icon (🗑️) next to any conversation in the sidebar.

### Organization

Conversations are sorted with the most recently updated at the top.

## Model Settings

Click the "Settings" expander to access model settings:

### Provider Selection

Choose between:
- OpenAI (GPT models)
- Anthropic (Claude models)

### Model Selection

Select a specific model from the chosen provider:

#### OpenAI Models
- **gpt-3.5-turbo**: Faster and more cost-effective
- **gpt-4**: More capable for complex tasks

#### Anthropic Models
- **claude-3-opus**: Most powerful model
- **claude-3-sonnet**: Balanced performance and speed
- **claude-3-haiku**: Fastest model, good for simple tasks

### Temperature

Adjust the "temperature" setting (0.0 to 1.0):
- **Lower values** (0.0-0.3): More consistent, deterministic responses
- **Medium values** (0.4-0.7): Balanced creativity and coherence
- **Higher values** (0.8-1.0): More creative, varied, and unpredictable responses

### Max Response Length

Set the maximum length for AI responses (100-4000 tokens).

## Import and Export

### Exporting Conversations

To save a conversation for backup or sharing:

1. Select the conversation you want to export
2. Click "Export Current Conversation" in the sidebar
3. The conversation will be saved as a JSON file in your Downloads folder

### Importing Conversations

To import a previously exported conversation:

1. Click "Browse files" under "Import Conversation" in the sidebar
2. Select the JSON file you want to import
3. The conversation will be added to your list

## Troubleshooting

### Common Issues

#### API Key Errors

If you see "API key not configured" errors:
1. Check that your .env file contains the correct API key
2. Verify that the key hasn't expired
3. Restart the application after making changes to the .env file

#### Database Issues

If conversations aren't saving properly:
1. Check permissions on the `~/.zerocode-llm-chat` directory
2. If the database becomes corrupted, you can delete the `chat_history.db` file (note: this will erase all conversations)

#### Model Not Found Errors

If you receive "model not found" errors:
1. Verify that you have the correct API key for the selected provider
2. Check that the model you're trying to use is available with your subscription
3. Model names and versions may change; check the provider's documentation

### Data Locations

- **Configuration**: `.env` file in the application directory
- **Database**: `~/.zerocode-llm-chat/chat_history.db` (Linux/macOS) or `C:\Users\YourUsername\.zerocode-llm-chat\chat_history.db` (Windows)
- **Exports**: Saved to your Downloads folder by default

## Electron Usage

### Using the Electron Version

If you're using the Electron desktop version:

1. Installation is simplified - just download and run the installer for your platform
2. API keys are stored in the application's secure storage
3. The database is stored in the application's data directory
4. Updates can be installed automatically

### Converting from Streamlit to Electron

For developers looking to package this as an Electron application:

1. The SQLite database can be easily relocated to the Electron app's data directory
2. The UI is responsive and will work well in an Electron window
3. Consider implementing a secure storage solution for API keys
4. Add a configuration page in the Electron app for API key management

## Advanced Features

### Custom Database Location

To use a custom location for the database, modify `src/db/db_manager.py` to specify your preferred path.

### Adding New Model Providers

Developers can extend the `src/llm/chat_client.py` file to add support for additional providers.
