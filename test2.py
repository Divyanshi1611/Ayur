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
    .chat-container {
        height: 60vh;
        overflow-y: auto;
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        margin-bottom: 1rem;
        border: 1px solid #dee2e6;
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
        margin-left: 20%;
    }
    .bot-message {
        background-color: #f0f2f6;
        margin-right: 20%;
    }
    .message-content {
        margin-left: 1rem;
    }
    .input-container {
        position: fixed;
        bottom: 0;
        width: 100%;
        padding: 1rem;
        background-color: white;
        border-top: 1px solid #dee2e6;
    }
    .avatar {
        font-size: 1.5rem;
    }
    .booking-button {
        margin-top: 1rem;
        padding: 0.5rem 1rem;
        background-color: #28a745;
        color: white;
        border-radius: 0.3rem;
        text-align: center;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

def get_response(question):
    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        prompt = f"""
        As a health assistant, provide information about {question}. 
        If describing symptoms or health conditions, include:
        1. Common treatments and home remedies
        2. When to see a doctor
        3. Preventive measures

        End the response with:
        ---
        🏥 Need professional help? Consider booking an appointment with a specialist.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def init():
    if os.getenv("GOOGLE_API_KEY") is None or os.getenv("GOOGLE_API_KEY")=="":
        st.error("API Key is not set! Please check your .env file.")
        st.stop()

def handle_booking():
    st.session_state['booking'] = True
    booking_form = """
    ### Book an Appointment
    Please fill in your details:
    """
    st.markdown(booking_form)
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    date = st.date_input("Preferred Date")
    if st.button("Confirm Booking"):
        st.success("Appointment request submitted! We'll contact you shortly.")
        st.session_state['booking'] = False

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
        - Appointment booking
        
        **Note:** This is not a replacement for professional medical advice.
        """)
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state['chat_history'] = []
            st.experimental_rerun()
    
    # Main content
    st.title("👩‍⚕️ AYUR - Your Health Assistant")
    st.markdown("---")

    # Initialize session states
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'booking' not in st.session_state:
        st.session_state['booking'] = False

    # Display booking form if requested
    if st.session_state.get('booking', False):
        handle_booking()
        return

    # Chat interface
    chat_container = st.container()
    input_container = st.container()

    # Display chat history
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)

   # ...existing code...

    # Input area
    with input_container:
        col1, col2 = st.columns([4, 1])
        with col1:
            # Initialize the session state for user input if not exists
            if "user_input" not in st.session_state:
                st.session_state.user_input = ""
            
            user_input = st.text_input(
                "Type your health-related question here:", 
                placeholder="Ex: What are the symptoms of common cold?",
                key="user_input"
            )
        with col2:
            submit = st.button("Ask AYUR 🔍", use_container_width=True)

        # Handle form submission
        if user_input and submit:
            # Store the current input
            current_input = user_input
            
            # Add message to chat history
            st.session_state['chat_history'].append({
                "role": "user", 
                "content": current_input
            })
            
            with st.spinner("AYUR is thinking..."):
                response = get_response(current_input)
                if response:
                    st.session_state['chat_history'].append({
                        "role": "assistant", 
                        "content": response
                    })
                    
                    # Show booking button if health condition is mentioned
                    if any(word in response.lower() for word in ['symptom', 'condition', 'syndrome', 'disease']):
                        if st.button("📅 Book an Appointment"):
                            st.session_state['booking'] = True
                            st.experimental_rerun()
            
            # Reset the input using form_submit_button
            st.session_state.user_input = ""
            st.experimental_rerun()

# ...existing code...
if __name__ == "__main__":
    main()