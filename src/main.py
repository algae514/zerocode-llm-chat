"""
ZeroCode LLM Chat Client - Main Entry Point
"""
import os
import streamlit as st
from dotenv import load_dotenv
from src.llm.chat_client import ChatClient
from src.ui.chat_interface import ChatInterface

def main():
    """Main application entry point"""
    # Load environment variables
    load_dotenv()
    
    # Set up Streamlit page
    st.set_page_config(
        page_title="ZeroCode LLM Chat",
        page_icon="💬",
        layout="wide"
    )
    
    # Check for API keys
    openai_api_key = os.getenv("OPENAI_API_KEY")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not openai_api_key and not anthropic_api_key:
        st.error("No API keys found. Please add at least one provider API key to your .env file.")
        st.info("You need either OPENAI_API_KEY or ANTHROPIC_API_KEY (or both) to use this application.")
        st.write("""
        ## How to Set Up API Keys
        
        1. Create a `.env` file in the root directory of this project
        2. Add your API keys to the file in this format:
        ```
        OPENAI_API_KEY=your_openai_key_here
        ANTHROPIC_API_KEY=your_anthropic_key_here
        ```
        3. Restart the application
        """)
        st.stop()
    
    # Create chat client instance
    # Default to OpenAI if available, otherwise use Anthropic
    default_model = "gpt-3.5-turbo" if openai_api_key else "claude-3-sonnet"
    chat_client = ChatClient(model=default_model)
    
    # Initialize the UI
    chat_interface = ChatInterface(chat_client)
    
    # Run the interface
    chat_interface.run()

if __name__ == "__main__":
    main()
