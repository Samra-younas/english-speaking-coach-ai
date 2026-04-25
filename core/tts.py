import tempfile
import asyncio
import edge_tts
from config import VOICE


async def _speak_async(text):
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    await edge_tts.Communicate(text, VOICE).save(tmp.name)
    return tmp.name


def speak(text):
    """Converts text to speech and returns path to the MP3 file."""
    try:
        return asyncio.run(_speak_async(text))
    except Exception as e:
        print(f"TTS error: {e}")
        return None