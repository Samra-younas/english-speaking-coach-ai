import streamlit as st
from groq import Groq


def load_model():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])


def transcribe(client, audio_path):
    with open(audio_path, "rb") as f:
        result = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=f,
        )
    return result.text