import streamlit as st
import requests
from streamlit_chat import message
from dotenv import load_dotenv
import google.generativeai as genai
import os
from langchain.chat_models import ChatOpenAI

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel()

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
    

    

    with st.sidebar:
        user_input=st.text_input("Your message: ",key="user_input")
    if user_input:

  
   
if __name__=="__main__":
    main()
