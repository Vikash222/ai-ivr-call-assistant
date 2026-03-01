def build_summary(caller, text, decision):
    emoji = {
        "FORWARD": "✅",
        "REJECT": "❌",
        "ASK_MORE": "ℹ️"
    }.get(decision, "")

    return f"""
📞 Call Summary
Caller: {caller}
Said: {text}
Decision: {decision} {emoji}
"""