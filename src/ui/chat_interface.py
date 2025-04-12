"""
Chat Interface for the LLM Chat Client
"""
import streamlit as st
import os
from src.llm.chat_client import ChatClient

class ChatInterface:
    """Streamlit-based chat interface"""
    
    def __init__(self, chat_client: ChatClient):
        """
        Initialize the chat interface
        
        Args:
            chat_client: Instance of the chat client
        """
        self.chat_client = chat_client
        
        # Initialize session state for chat history if it doesn't exist
        if "messages" not in st.session_state:
            st.session_state.messages = []
    
    def run(self):
        """Run the chat interface"""
        # Display the header
        st.title("ZeroCode LLM Chat")
        st.subheader("Have a conversation with an AI assistant")
        
        # Add model selection in the sidebar
        with st.sidebar:
            st.header("Settings")
            
            # Group models by provider
            provider = st.selectbox(
                "Select Provider",
                ["OpenAI", "Anthropic"]
            )
            
            # Display appropriate models based on provider
            if provider == "OpenAI":
                openai_models = ["gpt-3.5-turbo", "gpt-4"]
                model = st.selectbox("Select Model", openai_models)
                
                # Check if OpenAI API key is set
                if not os.getenv("OPENAI_API_KEY"):
                    st.error("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
            
            elif provider == "Anthropic":
                anthropic_models = ["claude-3-opus", "claude-3-sonnet", "claude-3-haiku"]
                model = st.selectbox("Select Model", anthropic_models)
                
                # Check if Anthropic API key is set
                if not os.getenv("ANTHROPIC_API_KEY"):
                    st.error("Anthropic API key not found. Please set ANTHROPIC_API_KEY in your .env file.")
                    st.info("You can get an API key from https://console.anthropic.com/")
            
            # Update the model in the chat client
            if model != self.chat_client.model:
                self.chat_client.model = model
            
            # Add a button to clear the chat history
            if st.button("Clear Chat History"):
                st.session_state.messages = []
                self.chat_client.clear_history()
                st.rerun()
                
            # Add temperature slider
            temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
            
            # Add maximum length slider
            max_tokens = st.slider("Max Response Length", min_value=100, max_value=4000, value=1000, step=100)
            
            # Display API status
            st.subheader("API Status")
            if os.getenv("OPENAI_API_KEY"):
                st.success("OpenAI: Connected")
            else:
                st.error("OpenAI: Not configured")
                
            if os.getenv("ANTHROPIC_API_KEY"):
                st.success("Anthropic: Connected")
            else:
                st.error("Anthropic: Not configured")
        
        # Display existing chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Handle user input
        if prompt := st.chat_input("Type your message here..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Get assistant response with a loading spinner
            with st.chat_message("assistant"):
                with st.spinner(f"Thinking using {model}..."):
                    response = self.chat_client.get_response(prompt)
                    st.markdown(response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
