# GALAT:
from turtle import st

# SAHI:
import streamlit as st
import anthropic
from config import SYSTEM_PROMPT

def get_client():
    return anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])