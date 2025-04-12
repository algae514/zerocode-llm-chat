"""
Chat Client for interacting with LLMs
"""
from openai import OpenAI
from typing import List, Dict, Any, Optional

class ChatClient:
    """Client for interacting with LLM APIs"""
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize the chat client
        
        Args:
            api_key: API key for the LLM provider
            model: Model to use for chat (default: gpt-3.5-turbo)
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.conversation_history = []
    
    def add_message(self, role: str, content: str):
        """
        Add a message to the conversation history
        
        Args:
            role: The role of the message sender ('user' or 'assistant')
            content: The content of the message
        """
        self.conversation_history.append({"role": role, "content": content})
    
    def get_response(self, user_message: str) -> str:
        """
        Get a response from the LLM
        
        Args:
            user_message: The user's message
            
        Returns:
            The LLM's response as a string
        """
        # Add the user message to the history
        self.add_message("user", user_message)
        
        # Get response from OpenAI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            temperature=0.7,
            max_tokens=1000
        )
        
        # Extract the response text
        response_text = response.choices[0].message.content
        
        # Add the assistant's response to history
        self.add_message("assistant", response_text)
        
        return response_text
    
    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
