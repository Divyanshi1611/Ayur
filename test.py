import streamlit as st
import requests
from streamlit_chat import message
from dotenv import load_dotenv
import google.generativeai as genai
import os
from langchain.chat_models import ChatOpenAI

# Initialize and configure
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Set page configuration
st.set_page_config(
    page_title="AYUR - Your Health Assistant",
    page_icon="👩‍⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput {
        margin-bottom: 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
    }
    .user-message {
        background-color: #e6f3ff;
    }
    .bot-message {
        background-color: #f0f2f6;
    }
    .message-content {
        margin-left: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def init():
    if os.getenv("GOOGLE_API_KEY") is None or os.getenv("GOOGLE_API_KEY")=="":
        st.error("API Key is not set! Please check your .env file.")
        st.stop()

def get_response(question):
    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def main():
    init()
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/caduceus.png")
        st.title("AYUR")
        st.markdown("---")
        st.markdown("""
        ### About
        AYUR is your personal health assistant powered by AI. 
        Feel free to ask any health-related questions!
        
        ### Features
        - 24/7 availability
        - Personalized responses
        - Medical information
        - Health tips
        
        **Note:** This is not a replacement for professional medical advice.
        """)
        
    # Main content
    st.title("👩‍⚕️ AYUR - Your Health Assistant")
    st.markdown("---")

    # Initialize session state
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Chat interface
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("Type your health-related question here:", 
                                 placeholder="Ex: What are the symptoms of common cold?",
                                 key="user_input")
    with col2:
        submit = st.button("Ask AYUR 🔍", use_container_width=True)

    # Handle conversation
    if submit and user_input:
        # Add user message to chat
        st.session_state['chat_history'].append({"role": "user", "content": user_input})
        
        with st.spinner("AYUR is thinking..."):
            response = get_response(user_input)
            if response:
                st.session_state['chat_history'].append({"role": "assistant", "content": response})

    # Display chat history
    if st.session_state['chat_history']:
        st.markdown("### Conversation History")
        for message in st.session_state['chat_history']:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <div class="avatar">👤</div>
                    <div class="message-content">{message["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message bot-message">
                    <div class="avatar">👩‍⚕️</div>
                    <div class="message-content">{message["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Clear chat button
        if st.button("Clear Chat History"):
            st.session_state['chat_history'] = []
            st.experimental_rerun()

if __name__ == "__main__":
    main()