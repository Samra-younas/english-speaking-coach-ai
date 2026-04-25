import os
from groq import Groq

def load_model():
    """Returns Groq client — replaces Whisper."""
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe(client, path):
    """Transcribes audio file using Groq Whisper API."""
    with open(path, "rb") as f:
        result = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=f,
        )
    return result.text.strip()