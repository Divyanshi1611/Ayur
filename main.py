import streamlit as st
import requests
from streamlit_chat import message
from dotenv import load_dotenv
import google.generativeai as genai
import os
from langchain.chat_models import ChatOpenAI
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
chat=model.start_chat(history=[])

from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)
def init():
    load_dotenv()
    if os.getenv("GOOGLE_API_KEY") is None or os.getenv("GOOGLE_API_KEY")=="":
        print("API_KEY is not set")
        exit(1)
    else:
        print("API_KEY is set")
    st.set_page_config(
        page_title="Your own health assistant",
        page_icon="👩‍⚕️💊"
    
    )
def main():
    init()
    st.header("AYUR--Health assistant 👩‍⚕️")
    

    

   
    user_input=st.text_input("Your message: ",key="user_input")
    submit=st.button("Generate response")
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    def get_response(question):
        response = chat.send_message(question, stream=True)
        return response
    if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []
    if submit and user_input:
        response=get_response(user_input)
        st.session_state['chat_history'].append(user_input)
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(chunk.text)
    st.subheader("Your chat history is: ")

   
if __name__=="__main__":
    main()
