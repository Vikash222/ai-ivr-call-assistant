import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

if not ACCOUNT_SID or not AUTH_TOKEN:
    raise RuntimeError("Twilio credentials not found in environment")

FROM_WHATSAPP = "whatsapp:+141558886"
TO_WHATSAPP = "whatsapp:+917436"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(text):
    msg = client.messages.create(
        body=text,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )
    print("✅ WhatsApp sent:", msg.sid)