import requests
import sounddevice as sd
import whisper
from scipy.io.wavfile import write

SAMPLE_RATE = 16000
DURATION = 5
API_URL = "http://127.0.0.1:8000/ivr/call"

def record_audio():
    print("🎙️ Speak now (5 seconds)...")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    print("✅ Recording done")
    return audio

def normalize(text: str) -> str:
    t = text.lower()
    replacements = {
        "bhai": "",
        "pls": "please",
        "plz": "please",
        "kaam": "work",
        "project discuss": "project discussion",
        "loan offer": "loan",
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t

def speech_to_text():
    audio = record_audio()
    write("temp.wav", SAMPLE_RATE, audio)

    print("🧠 Transcribing...")
    model = whisper.load_model("base")

    # 👇 RESULT YAHAN DEFINE HOTA HAI
    result = model.transcribe(
        "temp.wav",
        language="en",
        task="transcribe",
        initial_prompt="This is a phone call about work, projects, or services."
    )

    text = result["text"].strip()
    return text

if __name__ == "__main__":
    text = speech_to_text()

    if not text or len(text) < 3:
        print("⚠️ Low confidence speech, please speak again.")
        exit(0)

    text = normalize(text)
    print("📝 You said:", text)

    payload = {
        "caller_number": "MIC_CALLER",
        "speech_text": text
    }

    response = requests.post(API_URL, json=payload)
    print("📨 API Response:", response.json())