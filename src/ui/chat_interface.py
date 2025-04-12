"""
Chat Interface for the LLM Chat Client
"""
import streamlit as st
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
            model = st.selectbox(
                "Select Model",
                ["gpt-3.5-turbo", "gpt-4", "claude-3-opus", "claude-3-sonnet"]
            )
            
            # Update the model in the chat client
            if model != self.chat_client.model:
                self.chat_client.model = model
            
            # Add a button to clear the chat history
            if st.button("Clear Chat History"):
                st.session_state.messages = []
                self.chat_client.clear_history()
                st.rerun()
        
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
                with st.spinner("Thinking..."):
                    response = self.chat_client.get_response(prompt)
                    st.markdown(response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
