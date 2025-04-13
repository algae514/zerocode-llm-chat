"""
Chat Interface for the LLM Chat Client
"""
import streamlit as st
import os
import time
from datetime import datetime
from typing import List, Dict, Any
from src.llm.chat_client import ChatClient
from src.db.db_manager import DBManager

class ChatInterface:
    """Streamlit-based chat interface"""
    
    def __init__(self, chat_client: ChatClient, db_manager: DBManager):
        """
        Initialize the chat interface
        
        Args:
            chat_client: Instance of the chat client
            db_manager: Instance of the database manager
        """
        self.chat_client = chat_client
        self.db_manager = db_manager
        
        # Initialize session state variables if they don't exist
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        if "current_conversation_id" not in st.session_state:
            # Create a new conversation by default
            conversation_id = self.db_manager.create_conversation(model=self.chat_client.model)
            st.session_state.current_conversation_id = conversation_id
            
        if "conversation_title" not in st.session_state:
            st.session_state.conversation_title = f"New Conversation {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            
        if "show_sidebar" not in st.session_state:
            st.session_state.show_sidebar = True
    
    def load_conversation(self, conversation_id: str):
        """Load a conversation from the database"""
        conversation, messages = self.db_manager.get_conversation(conversation_id)
        
        if conversation:
            # Update session state
            st.session_state.current_conversation_id = conversation_id
            st.session_state.conversation_title = conversation["title"]
            
            # Convert DB messages to the format expected by the UI
            ui_messages = []
            for msg in messages:
                ui_messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            
            st.session_state.messages = ui_messages
            
            # Update the chat client's conversation history
            self.chat_client.conversation_history = ui_messages.copy()
            
            # Update the model if it's different
            if conversation["model"] != self.chat_client.model:
                self.chat_client.model = conversation["model"]
    
    def toggle_sidebar(self):
        """Toggle the sidebar visibility"""
        st.session_state.show_sidebar = not st.session_state.show_sidebar
    
    def run(self):
        """Run the chat interface"""
        # Set up the layout with columns for the chat history sidebar and the main chat
        if st.session_state.show_sidebar:
            sidebar_col, main_col = st.columns([1, 3])
        else:
            main_col = st
        
        # Sidebar for conversation management
        if st.session_state.show_sidebar:
            with sidebar_col:
                st.button("Hide Conversations", on_click=self.toggle_sidebar)
                
                st.subheader("Conversations")
                
                # Button to create a new conversation
                if st.button("New Conversation"):
                    # Create a new conversation
                    conversation_id = self.db_manager.create_conversation(model=self.chat_client.model)
                    st.session_state.current_conversation_id = conversation_id
                    st.session_state.conversation_title = f"New Conversation {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                    st.session_state.messages = []
                    self.chat_client.clear_history()
                    st.rerun()
                
                # Get all conversations
                conversations = self.db_manager.get_all_conversations()
                
                # Display the list of conversations
                for conversation in conversations:
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        # Show the title or summary and highlight the current conversation
                        if conversation["id"] == st.session_state.current_conversation_id:
                            st.markdown(f"**👉 {conversation['title']}**")
                        else:
                            # Make the title clickable to load the conversation
                            if st.button(f"{conversation['title']}", key=f"load_{conversation['id']}"):
                                self.load_conversation(conversation["id"])
                                st.rerun()
                    
                    # Delete button
                    with col2:
                        if st.button("🗑️", key=f"delete_{conversation['id']}"):
                            # Confirm before deleting
                            if conversation["id"] == st.session_state.current_conversation_id:
                                # If deleting current conversation, create a new one
                                self.db_manager.delete_conversation(conversation["id"])
                                conversation_id = self.db_manager.create_conversation(model=self.chat_client.model)
                                st.session_state.current_conversation_id = conversation_id
                                st.session_state.conversation_title = f"New Conversation {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                                st.session_state.messages = []
                                self.chat_client.clear_history()
                            else:
                                # Just delete the conversation
                                self.db_manager.delete_conversation(conversation["id"])
                            st.rerun()
                
                # Divider between conversation list and settings
                st.divider()
                
                # Export/Import options
                st.subheader("Import/Export")
                
                # Export current conversation
                if st.button("Export Current Conversation"):
                    # Use a timestamp for the filename
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"conversation_{timestamp}.json"
                    home_dir = os.path.expanduser("~")
                    export_path = os.path.join(home_dir, "Downloads", filename)
                    
                    if self.db_manager.export_conversation(st.session_state.current_conversation_id, export_path):
                        st.success(f"Conversation exported to {export_path}")
                    else:
                        st.error("Failed to export conversation")
                
                # Import conversation
                uploaded_file = st.file_uploader("Import Conversation", type=["json"])
                if uploaded_file is not None:
                    # Save the uploaded file temporarily
                    import tempfile
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
                        tmp.write(uploaded_file.getvalue())
                        temp_path = tmp.name
                    
                    # Import the conversation
                    conversation_id = self.db_manager.import_conversation(temp_path)
                    
                    # Clean up the temporary file
                    os.unlink(temp_path)
                    
                    if conversation_id:
                        st.success("Conversation imported successfully")
                        # Load the imported conversation
                        self.load_conversation(conversation_id)
                        st.rerun()
                    else:
                        st.error("Failed to import conversation")
        
        # Main chat area
        with main_col:
            # Header with conversation title and sidebar toggle
            col1, col2 = st.columns([3, 1])
            with col1:
                # Make the title editable
                new_title = st.text_input("Conversation Title", value=st.session_state.conversation_title)
                if new_title != st.session_state.conversation_title:
                    st.session_state.conversation_title = new_title
                    self.db_manager.update_conversation_title(st.session_state.current_conversation_id, new_title)
            
            with col2:
                if not st.session_state.show_sidebar:
                    st.button("Show Conversations", on_click=self.toggle_sidebar)
            
            # Model selection and settings
            with st.expander("Settings"):
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
                    anthropic_models = ["claude-3-opus", "claude-3-sonnet", "claude-3-haiku", "claude-3-7-sonnet"]
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
                    # Clear the chat history but keep the conversation
                    st.session_state.messages = []
                    self.chat_client.clear_history()
                    
                    # Create a new conversation
                    conversation_id = self.db_manager.create_conversation(
                        title=st.session_state.conversation_title,
                        model=self.chat_client.model
                    )
                    st.session_state.current_conversation_id = conversation_id
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
            
            # Divider before the chat
            st.divider()
            
            # Display existing chat messages
            for i, message in enumerate(st.session_state.messages):
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # Handle user input
            if prompt := st.chat_input("Type your message here..."):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})
                
                # Save the message to the database
                self.db_manager.add_message(
                    st.session_state.current_conversation_id,
                    "user",
                    prompt
                )
                
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
                
                # Save the response to the database
                self.db_manager.add_message(
                    st.session_state.current_conversation_id,
                    "assistant",
                    response
                )
