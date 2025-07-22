# Chatbot
An interactive Python project that allows users to talk to an AI using their voice. The AI listens to your speech, transcribes it to text, sends it to a language model (Cohere), and plays back the AI’s spoken response.

## 🚀 Features

-This project is a fully interactive voice-based AI assistant that allows users to:

-Speak freely using a microphone

-Automatically transcribe their voice to text

-Get intelligent responses using the Cohere AI model

-Hear the AI reply via Text-to-Speech (TTS)

.

🔧 Technologies Used


| Component        | Description                             |
| ---------------- | --------------------------------------- |
| 🧠 Whisper       | Speech-to-text transcription (ASR)      |
| 🧠 Cohere        | Large language model (text generation)  |
| 🗣️ gTTS         | Text-to-speech conversion (AI voice)    |
| 🎧 sounddevice   | Audio recording from microphone         |
| 🔉 playsound     | Simple playback of MP3 files            |
| 🎚️ NumPy, SciPy | Audio processing and manipulation       |
| 🧪 FFmpeg        | Audio decoding and conversion (backend) |

⚙️ Installation
✅ Prerequisites
Python 3.10+

Anaconda / Miniconda

Working microphone

Stable internet connection


🧪 Flow:
You speak → voice is recorded (WAV format)

Whisper transcribes your voice to text

Text is sent to Cohere AI model

The AI generates a reply

gTTS converts the reply to voice

Voice is played back to the user







- 
