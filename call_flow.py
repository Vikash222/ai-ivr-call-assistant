print("🔥 call_flow.py STARTED")

from decision_engine import decide_call
from notifier import build_summary
from whatsapp_notifier import send_whatsapp_message


def simulate_call(caller_name, spoken_text):
    print("\n📞 Incoming Call")
    print("Caller:", caller_name)
    print("Says:", spoken_text)

    decision = decide_call(spoken_text)
    summary = build_summary(caller_name, spoken_text, decision)

    print("\n📩 WhatsApp Summary:")
    print(summary)

    send_whatsapp_message(summary)


if __name__ == "__main__":
    print("▶ Running main block")
    simulate_call("Unknown", "urgent project discussion please help")
    simulate_call("Unknown", "free loan offer limited time")
    simulate_call("Unknown", "hello I want to talk")