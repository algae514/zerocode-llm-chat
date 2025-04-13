# Developer Guide

This guide provides information for developers who want to extend or modify the ZeroCode LLM Chat Client.

## Table of Contents
- [Project Structure](#project-structure)
- [Key Components](#key-components)
- [Adding New Models](#adding-new-models)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Electron Integration](#electron-integration)
- [Contributing](#contributing)

## Project Structure

```
zerocode/
├── docs/                    # Documentation
│   ├── api_keys.md          # Guide for obtaining API keys
│   ├── developer.md         # Developer documentation
│   ├── images/              # Documentation images
│   └── usage.md             # User guide
├── src/                     # Source code
│   ├── __init__.py
│   ├── db/                  # Database and storage modules
│   │   ├── __init__.py
│   │   └── db_manager.py    # SQLite database manager
│   ├── llm/                 # LLM integration modules
│   │   ├── __init__.py
│   │   ├── chat_client.py   # Main chat client class
│   │   └── llm_factory.py   # Factory for creating LLM clients
│   ├── ui/                  # UI components
│   │   ├── __init__.py
│   │   └── chat_interface.py # Streamlit UI interface
│   └── main.py              # Application entry point
├── tests/                   # Test files
│   ├── __init__.py
│   └── test_chat_client.py  # Tests for chat client
├── .env                     # Environment variables (not in git)
├── .env.example             # Example environment file
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
├── setup.py                 # Python package setup
├── setup.sh                 # Setup script for Linux/macOS
├── setup.bat                # Setup script for Windows
├── start.sh                 # Start script for Linux/macOS
├── start.bat                # Start script for Windows
└── README.md                # Project documentation
```

## Key Components

### ChatClient (src/llm/chat_client.py)

The `ChatClient` class handles communication with LLM APIs:

- Maintains conversation history
- Maps model names to API-specific versions
- Handles routing requests to the appropriate provider
- Formats messages according to each provider's requirements

To extend with a new provider:
1. Add a new section to the `get_response()` method
2. Map display model names to API model names
3. Format messages according to the provider's API requirements

### DBManager (src/db/db_manager.py)

The `DBManager` class handles persistent storage:

- Creates and manages a SQLite database
- Provides methods for conversation CRUD operations
- Handles import/export functionality

To modify the storage:
1. Update the `_init_db()` method to change the schema
2. Modify CRUD methods as needed
3. Consider migration code for existing databases

### ChatInterface (src/ui/chat_interface.py)

The `ChatInterface` class manages the Streamlit UI:

- Renders the conversation sidebar
- Displays chat messages
- Handles user inputs
- Manages conversation switching

To modify the UI:
1. Update the `run()` method
2. Use Streamlit components to create new UI elements
3. Connect UI actions to backend functionality

## Adding New Models

To add support for a new LLM provider:

1. Update `requirements.txt` to include the provider's Python library
2. Modify `ChatClient` to include the new provider logic
3. Add a new provider section in `chat_interface.py`
4. Update documentation to reflect the new provider

Example code for adding a new provider:

```python
# In chat_client.py
elif self.model.startswith("new-provider"):
    # New provider models
    if not self.new_provider_api_key:
        return "Error: New Provider API key not configured."
    
    try:
        # Import required library
        import new_provider_lib
        
        # Create client
        client = new_provider_lib.Client(api_key=self.new_provider_api_key)
        
        # Format messages
        formatted_messages = self._format_messages_for_new_provider(self.conversation_history)
        
        # Make API call
        response = client.create_completion(
            model=self.model,
            messages=formatted_messages,
            temperature=0.7
        )
        
        # Extract response text
        response_text = response.choices[0].message.content
    except Exception as e:
        response_text = f"Error calling New Provider API: {str(e)}"
```

## Database Schema

The SQLite database uses the following schema:

### Conversations Table

```sql
CREATE TABLE conversations (
    id TEXT PRIMARY KEY,
    title TEXT,
    model TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    summary TEXT
)
```

### Messages Table

```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id TEXT,
    role TEXT,
    content TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversations (id)
)
```

To view the database directly:
```bash
sqlite3 ~/.zerocode-llm-chat/chat_history.db
```

Common SQLite commands:
```sql
.tables                           -- List all tables
SELECT * FROM conversations;      -- View all conversations
SELECT * FROM messages LIMIT 10;  -- View 10 messages
```

## Testing

The project includes unit tests in the `tests/` directory.

To run the tests:

```bash
# From the project root
python -m unittest discover tests
```

When adding new features, please include appropriate tests.

## Electron Integration

To package the application with Electron:

1. Create a JavaScript wrapper using Electron
2. Adjust database paths to use Electron's app data directory
3. Implement secure storage for API keys
4. Handle application lifecycle events

Key considerations for Electron:
- Use the Electron app's user data directory for the SQLite database
- Handle window state persistence
- Implement proper error handling for Python process

## Contributing

We welcome contributions to improve ZeroCode:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Code Style

- Follow PEP 8 for Python code
- Use docstrings for all classes and methods
- Keep functions focused on a single responsibility
- Comment complex logic

### Pull Request Process

1. Update documentation to reflect your changes
2. Update the README.md if necessary
3. Your PR should reference any related issues
4. Wait for a maintainer to review and merge your PR
