import numpy as np
import tempfile
import soundfile as sf
from config import SAMPLE_RATE


def save_audio(chunks):
    audio = np.concatenate(chunks, axis=0)
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    sf.write(tmp.name, audio, SAMPLE_RATE)
    return tmp.name