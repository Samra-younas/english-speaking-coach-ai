import streamlit as st
import anthropic
from config import SYSTEM_PROMPT


def get_client():
    return anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])


def ask_claude(client, user_text, chat_history):
    chat_history.append({"role": "user", "content": user_text})
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=chat_history
    )
    reply = response.content[0].text
    chat_history.append({"role": "assistant", "content": reply})
    return reply, chat_history