"""
Chat Client for interacting with LLMs
"""
from openai import OpenAI
from typing import List, Dict, Any, Optional
import os
import streamlit as st

class ChatClient:
    """Client for interacting with LLM APIs"""
    
    # Mapping from display names to actual API model names
    ANTHROPIC_MODEL_MAP = {
        "claude-3-opus": "claude-3-opus-20240229",
        "claude-3-sonnet": "claude-3-sonnet-20240229",
        "claude-3-haiku": "claude-3-haiku-20240307",
        "claude-3-7-sonnet": "claude-3-7-sonnet-20250219"
    }
    
    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        """
        Initialize the chat client
        
        Args:
            api_key: API key for the LLM provider (default: None, will use environment variables)
            model: Model to use for chat (default: gpt-3.5-turbo)
        """
        self.openai_api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model = model
        self.conversation_history = []
        
        # Initialize OpenAI client
        if self.openai_api_key:
            self.openai_client = OpenAI(api_key=self.openai_api_key)
        else:
            self.openai_client = None
            
        # We'll initialize other clients as needed
    
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
        
        # Determine which provider to use based on the model
        if self.model.startswith("gpt"):
            # Using OpenAI
            if not self.openai_client:
                return "Error: OpenAI API key not configured. Please add it to your .env file."
            
            try:
                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=self.conversation_history,
                    temperature=0.7,
                    max_tokens=1000
                )
                
                response_text = response.choices[0].message.content
            except Exception as e:
                response_text = f"Error calling OpenAI API: {str(e)}"
                
        elif self.model.startswith("claude"):
            # Claude models
            if not self.anthropic_api_key:
                return "Error: Anthropic API key not configured. Please add ANTHROPIC_API_KEY to your .env file."
            
            try:
                # Import Anthropic library only when needed
                import anthropic
                
                # Convert conversation history to Anthropic format
                messages = []
                for msg in self.conversation_history:
                    if msg["role"] == "user":
                        messages.append({"role": "user", "content": msg["content"]})
                    elif msg["role"] == "assistant":
                        messages.append({"role": "assistant", "content": msg["content"]})
                
                # Create Anthropic client
                anthropic_client = anthropic.Anthropic(api_key=self.anthropic_api_key)
                
                # Map the display model name to the actual API model name
                actual_model = self.ANTHROPIC_MODEL_MAP.get(self.model, self.model)
                
                # Debug information
                print(f"Using Anthropic model: {actual_model}")
                
                response = anthropic_client.messages.create(
                    model=actual_model,
                    messages=messages,
                    max_tokens=1000
                )
                
                response_text = response.content[0].text
            except ImportError:
                response_text = "Error: The Anthropic Python library is not installed. Please run: pip install anthropic"
            except Exception as e:
                response_text = f"Error calling Anthropic API: {str(e)}"
        else:
            response_text = f"Unsupported model: {self.model}. Please select a different model."
        
        # Add the assistant's response to history
        self.add_message("assistant", response_text)
        
        return response_text
    
    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
