"""
Factory class for creating LLM clients based on provider
"""
import os
from typing import Optional, Dict, Any
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI as LangchainChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMFactory:
    """Factory for creating LLM clients"""
    
    @staticmethod
    def create_client(provider: str = "openai", model: Optional[str] = None) -> Any:
        """
        Create and return an LLM client based on the provider
        
        Args:
            provider: The LLM provider (e.g., 'openai', 'anthropic')
            model: The specific model to use (optional)
            
        Returns:
            An instance of the appropriate LLM client
        """
        if provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OpenAI API key not found in environment variables")
            
            # Default model if not specified
            if not model:
                model = "gpt-3.5-turbo"
                
            return OpenAI(api_key=api_key)
        
        elif provider == "anthropic":
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("Anthropic API key not found in environment variables")
            
            # Note: This is a placeholder as direct Anthropic API integration would need their SDK
            # Use Langchain for now as an example
            if not model:
                model = "claude-3-opus"
                
            # This is a placeholder for actual Anthropic client implementation
            # In a real implementation, you would use Anthropic's Python client
            raise NotImplementedError("Anthropic direct client not implemented yet")
        
        elif provider == "langchain-openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OpenAI API key not found in environment variables")
            
            if not model:
                model = "gpt-3.5-turbo"
                
            return LangchainChatOpenAI(openai_api_key=api_key, model_name=model)
            
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")
