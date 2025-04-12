"""
Tests for the ChatClient class
"""
import unittest
from unittest.mock import patch, MagicMock
from src.llm.chat_client import ChatClient

class TestChatClient(unittest.TestCase):
    """Test cases for the ChatClient class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.api_key = "test_api_key"
        with patch('openai.OpenAI'):
            self.chat_client = ChatClient(api_key=self.api_key)
    
    def test_add_message(self):
        """Test adding a message to the conversation history"""
        self.chat_client.add_message("user", "Hello, world!")
        self.assertEqual(len(self.chat_client.conversation_history), 1)
        self.assertEqual(self.chat_client.conversation_history[0]["role"], "user")
        self.assertEqual(self.chat_client.conversation_history[0]["content"], "Hello, world!")
    
    def test_clear_history(self):
        """Test clearing the conversation history"""
        self.chat_client.add_message("user", "Hello, world!")
        self.chat_client.clear_history()
        self.assertEqual(len(self.chat_client.conversation_history), 0)
    
    @patch('openai.OpenAI')
    def test_get_response(self, mock_openai):
        """Test getting a response from the LLM"""
        # Set up the mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock()]
        mock_completion.choices[0].message.content = "Test response"
        
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Create a new chat client with the mocked OpenAI
        chat_client = ChatClient(api_key=self.api_key)
        
        # Test getting a response
        response = chat_client.get_response("Test message")
        
        # Verify the response
        self.assertEqual(response, "Test response")
        
        # Verify that the message was added to history
        self.assertEqual(len(chat_client.conversation_history), 2)
        self.assertEqual(chat_client.conversation_history[0]["role"], "user")
        self.assertEqual(chat_client.conversation_history[0]["content"], "Test message")
        self.assertEqual(chat_client.conversation_history[1]["role"], "assistant")
        self.assertEqual(chat_client.conversation_history[1]["content"], "Test response")

if __name__ == "__main__":
    unittest.main()
