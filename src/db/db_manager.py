"""
Database Manager for the ZeroCode LLM Chat Client
Handles saving and loading chat histories using SQLite
"""
import os
import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
import uuid

class DBManager:
    """Database Manager for chat history persistence"""
    
    def __init__(self, db_path: str = None):
        """
        Initialize the database manager
        
        Args:
            db_path: Path to SQLite database file (default: creates 'chat_history.db' in the user's home directory)
        """
        if db_path is None:
            # Create a data directory in the user's home directory
            home_dir = os.path.expanduser("~")
            app_dir = os.path.join(home_dir, ".zerocode-llm-chat")
            
            # Create directory if it doesn't exist
            if not os.path.exists(app_dir):
                os.makedirs(app_dir)
                
            self.db_path = os.path.join(app_dir, "chat_history.db")
        else:
            self.db_path = db_path
        
        # Initialize the database
        self._init_db()
    
    def _init_db(self):
        """Initialize the database and create tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create conversations table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            title TEXT,
            model TEXT,
            created_at TIMESTAMP,
            updated_at TIMESTAMP,
            summary TEXT
        )
        ''')
        
        # Create messages table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id TEXT,
            role TEXT,
            content TEXT,
            timestamp TIMESTAMP,
            FOREIGN KEY (conversation_id) REFERENCES conversations (id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_conversation(self, title: str = None, model: str = "gpt-3.5-turbo") -> str:
        """
        Create a new conversation
        
        Args:
            title: Title for the conversation (default: timestamp)
            model: The model used for the conversation
            
        Returns:
            The ID of the created conversation
        """
        if title is None:
            title = f"Conversation {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        conversation_id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO conversations (id, title, model, created_at, updated_at, summary) VALUES (?, ?, ?, ?, ?, ?)",
            (conversation_id, title, model, now, now, "")
        )
        
        conn.commit()
        conn.close()
        
        return conversation_id
    
    def add_message(self, conversation_id: str, role: str, content: str) -> int:
        """
        Add a message to a conversation
        
        Args:
            conversation_id: ID of the conversation to add the message to
            role: Role of the sender (user or assistant)
            content: Content of the message
            
        Returns:
            The ID of the created message
        """
        now = datetime.now().isoformat()
        
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Add the message
        cursor.execute(
            "INSERT INTO messages (conversation_id, role, content, timestamp) VALUES (?, ?, ?, ?)",
            (conversation_id, role, content, now)
        )
        
        message_id = cursor.lastrowid
        
        # Update the conversation's updated_at timestamp
        cursor.execute(
            "UPDATE conversations SET updated_at = ? WHERE id = ?",
            (now, conversation_id)
        )
        
        # If this is the first user message, use it as a summary
        cursor.execute(
            "SELECT COUNT(*) FROM messages WHERE conversation_id = ?",
            (conversation_id,)
        )
        count = cursor.fetchone()[0]
        
        if count == 1 and role == "user":
            # Use the first few words as a summary
            summary = content[:50] + ("..." if len(content) > 50 else "")
            cursor.execute(
                "UPDATE conversations SET summary = ? WHERE id = ?",
                (summary, conversation_id)
            )
            
        conn.commit()
        conn.close()
        
        return message_id
    
    def get_conversation(self, conversation_id: str) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Get a conversation and its messages
        
        Args:
            conversation_id: ID of the conversation to retrieve
            
        Returns:
            A tuple containing the conversation metadata and list of messages
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Get conversation metadata
        cursor.execute(
            "SELECT * FROM conversations WHERE id = ?",
            (conversation_id,)
        )
        conversation_row = cursor.fetchone()
        
        if not conversation_row:
            conn.close()
            return None, []
        
        conversation = dict(conversation_row)
        
        # Get messages
        cursor.execute(
            "SELECT * FROM messages WHERE conversation_id = ? ORDER BY timestamp",
            (conversation_id,)
        )
        message_rows = cursor.fetchall()
        
        messages = [dict(row) for row in message_rows]
        
        conn.close()
        
        return conversation, messages
    
    def get_all_conversations(self) -> List[Dict[str, Any]]:
        """
        Get all conversations
        
        Returns:
            A list of all conversations with metadata
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM conversations ORDER BY updated_at DESC"
        )
        conversation_rows = cursor.fetchall()
        
        conversations = [dict(row) for row in conversation_rows]
        
        conn.close()
        
        return conversations
    
    def delete_conversation(self, conversation_id: str) -> bool:
        """
        Delete a conversation and all its messages
        
        Args:
            conversation_id: ID of the conversation to delete
            
        Returns:
            True if successful, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Delete messages first due to foreign key constraint
            cursor.execute(
                "DELETE FROM messages WHERE conversation_id = ?",
                (conversation_id,)
            )
            
            # Delete the conversation
            cursor.execute(
                "DELETE FROM conversations WHERE id = ?",
                (conversation_id,)
            )
            
            conn.commit()
            result = True
        except Exception as e:
            print(f"Error deleting conversation: {e}")
            conn.rollback()
            result = False
        
        conn.close()
        
        return result
    
    def update_conversation_title(self, conversation_id: str, title: str) -> bool:
        """
        Update the title of a conversation
        
        Args:
            conversation_id: ID of the conversation to update
            title: New title for the conversation
            
        Returns:
            True if successful, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "UPDATE conversations SET title = ? WHERE id = ?",
                (title, conversation_id)
            )
            
            conn.commit()
            result = True
        except Exception as e:
            print(f"Error updating conversation title: {e}")
            conn.rollback()
            result = False
        
        conn.close()
        
        return result
    
    def export_conversation(self, conversation_id: str, file_path: str) -> bool:
        """
        Export a conversation to a JSON file
        
        Args:
            conversation_id: ID of the conversation to export
            file_path: Path to save the JSON file
            
        Returns:
            True if successful, False otherwise
        """
        conversation, messages = self.get_conversation(conversation_id)
        
        if not conversation:
            return False
        
        export_data = {
            "conversation": conversation,
            "messages": messages
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(export_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting conversation: {e}")
            return False
    
    def import_conversation(self, file_path: str) -> Optional[str]:
        """
        Import a conversation from a JSON file
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            The ID of the imported conversation if successful, None otherwise
        """
        try:
            with open(file_path, 'r') as f:
                import_data = json.load(f)
            
            conversation = import_data.get("conversation", {})
            messages = import_data.get("messages", [])
            
            # Create a new conversation ID
            conversation_id = str(uuid.uuid4())
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Insert the conversation
            now = datetime.now().isoformat()
            cursor.execute(
                """INSERT INTO conversations 
                   (id, title, model, created_at, updated_at, summary) 
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    conversation_id, 
                    conversation.get("title", f"Imported {now}"),
                    conversation.get("model", "unknown"),
                    conversation.get("created_at", now),
                    now,
                    conversation.get("summary", "")
                )
            )
            
            # Insert messages
            for message in messages:
                cursor.execute(
                    """INSERT INTO messages 
                       (conversation_id, role, content, timestamp) 
                       VALUES (?, ?, ?, ?)""",
                    (
                        conversation_id,
                        message.get("role", "user"),
                        message.get("content", ""),
                        message.get("timestamp", now)
                    )
                )
            
            conn.commit()
            conn.close()
            
            return conversation_id
            
        except Exception as e:
            print(f"Error importing conversation: {e}")
            return None
