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
    
    # Initialize the chat client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("No OpenAI API key found. Please set it in your .env file.")
        st.stop()
    
    # Create chat client instance
    chat_client = ChatClient(api_key=api_key)
    
    # Initialize the UI
    chat_interface = ChatInterface(chat_client)
    
    # Run the interface
    chat_interface.run()

if __name__ == "__main__":
    main()
