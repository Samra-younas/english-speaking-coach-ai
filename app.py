import streamlit as st
import tempfile

from core.transcriber import load_model, transcribe
from core.coach import get_client, ask_claude
from core.tts import speak


# --- CACHED RESOURCES ---
@st.cache_resource
def load_whisper():
    return load_model()

@st.cache_resource
def get_claude():
    return get_client()

model = load_whisper()
client = get_claude()


# --- SESSION STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "conversation" not in st.session_state:
    st.session_state.conversation = []
    st.session_state.conversation.append({
        "role": "assistant",
        "text": "Hey! 👋 I'm your English speaking coach. Which topic would you like to practice today — AI, career, daily life, or something else?"
    })
if "audio_path" not in st.session_state:
    st.session_state.audio_path = None
if "processing" not in st.session_state:
    st.session_state.processing = False
if "pending_audio" not in st.session_state:
    st.session_state.pending_audio = None


# --- UI ---
st.title("🎙️ AI English Speaking Coach")
st.caption("Speak English — get corrections, responses & career questions!")
st.markdown("---")

# Conversation history
if st.session_state.conversation:
    for entry in st.session_state.conversation:
        if entry["role"] == "user":
            st.chat_message("user").write(entry["text"])
        else:
            st.chat_message("assistant").write(entry["text"])
    st.markdown("---")

# Clear button
if st.button("🗑️ Clear", use_container_width=True):
    st.session_state.chat_history = []
    st.session_state.conversation = []
    st.session_state.audio_path = None
    st.session_state.processing = False
    st.session_state.pending_audio = None
    st.session_state.conversation.append({
        "role": "assistant",
        "text": "Hey! 👋 I'm your English speaking coach. Which topic would you like to practice today — AI, career, daily life, or something else?"
    })
    st.rerun()

# Play TTS audio (hidden player)
if st.session_state.audio_path:
    st.markdown("""
        <style>
        audio { display: none; }
        </style>
    """, unsafe_allow_html=True)
    st.audio(st.session_state.audio_path, autoplay=True)
    st.session_state.audio_path = None


# --- PROCESSING: Transcribe + Claude + TTS ---
if st.session_state.processing and st.session_state.pending_audio:
    audio_bytes = st.session_state.pending_audio

    with st.spinner("📝 Transcribing..."):
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        tmp.write(audio_bytes)
        tmp.flush()
        user_text = transcribe(model, tmp.name)

    if not user_text.strip():
        st.warning("⚠️ Could not hear you! Please try again.")
        st.session_state.processing = False
        st.session_state.pending_audio = None
        st.rerun()
    else:
        with st.spinner("🤖 Coach thinking..."):
            # Sahi order: (client, user_text, chat_history)
            reply, updated_history = ask_claude(client, user_text, st.session_state.chat_history)
            st.session_state.chat_history = updated_history

        with st.spinner("🔊 Generating audio..."):
            audio_path = speak(reply)

        st.session_state.conversation.append({"role": "user", "text": user_text})
        st.session_state.conversation.append({"role": "assistant", "text": reply})
        st.session_state.audio_path = audio_path
        st.session_state.processing = False
        st.session_state.pending_audio = None
        st.rerun()


# --- RECORD (sirf tab dikhao jab processing nahi chal rahi) ---
elif not st.session_state.processing:
    audio_input = st.audio_input("🎙️ Record your voice")

    if audio_input is not None:
        audio_bytes = audio_input.getvalue()

        if len(audio_bytes) < 1000:
            st.warning("⚠️ Recording too short! Please speak for at least 1-2 seconds.")
        else:
            st.session_state.pending_audio = audio_bytes
            st.session_state.processing = True
            st.rerun()