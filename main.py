from fastapi import FastAPI
from pydantic import BaseModel

from ivr_voice import hindi_reply
from tts_hindi import speak_hindi
from decision_engine import decide_call
from notifier import build_summary
from whatsapp_notifier import send_whatsapp_message

app = FastAPI()

class IVRRequest(BaseModel):
    caller_number: str
    speech_text: str

class IVRResponse(BaseModel):
    decision: str
    message: str

@app.post("/ivr/call", response_model=IVRResponse)
def handle_ivr_call(data: IVRRequest):
    print("🔔 IVR endpoint HIT")
    print("Caller:", data.caller_number)
    print("Speech:", data.speech_text)

    # 🧠 AI decision
    decision = decide_call(data.speech_text)
    print("🧠 Decision:", decision)

    # 📩 WhatsApp summary
    summary = build_summary(
        caller=data.caller_number,
        text=data.speech_text,
        decision=decision
    )
    print("📩 Sending WhatsApp...")
    send_whatsapp_message(summary)
    print("✅ WhatsApp sent")

    # 🗣️ HINDI IVR VOICE (⬅️ YAHI NAYA PART)
    voice_text = hindi_reply(decision)
    print("🗣️ IVR says:", voice_text)
    speak_hindi(voice_text)

    # 🌐 API response
    if decision == "FORWARD":
        msg = "Connecting your call. Please hold."
    elif decision == "REJECT":
        msg = "We are unable to process your call at this time."
    else:
        msg = "Please provide a bit more detail."

    return IVRResponse(decision=decision, message=msg)