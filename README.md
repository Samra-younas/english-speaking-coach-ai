# 🎙️ AI English Speaking Coach

An interactive voice-based English learning app powered by **Whisper**, **Claude AI**, and **Edge TTS**. Speak naturally, get instant grammar corrections, and practice real conversations with an AI coach named Alex.

---

## 🚀 Features

- 🎤 **Real-time voice recording** via your microphone
- 📝 **Speech-to-text transcription** using OpenAI Whisper
- 🤖 **AI coaching** powered by Anthropic Claude (grammar correction + follow-up questions)
- 🔊 **Text-to-speech replies** using Microsoft Edge TTS
- 💬 **Persistent conversation history** within each session
- 🧹 **One-click conversation reset**

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| STT | OpenAI Whisper (`base` model) |
| LLM | Anthropic Claude (`claude-sonnet-4-5`) |
| TTS | Microsoft Edge TTS (`en-US-JennyNeural`) |
| Audio I/O | SoundDevice + SoundFile |

---

## 📁 Project Structure

```
ai-english-coach/
├── app.py               # Main Streamlit application
├── .env                 # Environment variables (API keys) — not committed
├── .env.example         # Template for environment variables
├── requirements.txt     # Python dependencies
├── .gitignore           # Files to exclude from Git
└── README.md            # This file
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/Samra-younas/english-speaking-coach-ai]
cd ai-english-coach
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=your_api_key_here
```

Get your key at: https://console.anthropic.com/

### 5. Run the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🎮 How to Use

1. **Press `🎙️ START`** — your microphone starts recording
2. **Speak in English** — talk about any topic (AI, career, daily life, etc.)
3. **Press `⏹️ STOP`** — recording stops and processing begins
4. **Wait a moment** — the app transcribes, gets AI feedback, and plays audio
5. **Listen to Alex** — hear grammar corrections and a follow-up question
6. **Press `🗑️ Clear`** to reset and start a new session

---

## 🔑 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | ✅ Yes |

---

## 📦 Requirements

See `requirements.txt` for the full list. Key packages:

- `streamlit` — web UI
- `openai-whisper` — speech recognition
- `anthropic` — Claude AI client
- `edge-tts` — text-to-speech
- `sounddevice` — microphone access
- `soundfile` — audio file handling
- `numpy` — audio array processing
- `python-dotenv` — environment variable loading

---

## 🐛 Troubleshooting

**Microphone not working?**
- Make sure your browser/OS has microphone permissions enabled
- On Linux, you may need `portaudio`: `sudo apt install portaudio19-dev`

**Whisper download slow on first run?**
- The `base` model (~140MB) downloads automatically on first use

**TTS not playing audio?**
- Ensure your browser allows autoplay, or click the audio player manually

**`ANTHROPIC_API_KEY` error?**
- Make sure your `.env` file exists and the key is valid

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Anthropic Claude](https://www.anthropic.com/)
- [Microsoft Edge TTS](https://github.com/rany2/edge-tts)
- [Streamlit](https://streamlit.io/)
