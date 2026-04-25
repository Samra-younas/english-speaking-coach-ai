import streamlit as st
from groq import Groq

def load_model():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])