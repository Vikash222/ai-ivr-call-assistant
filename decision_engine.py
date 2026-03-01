def decide_call(text: str) -> str:
    text = text.lower()

    # ❌ Spam / Sales patterns
    spam_patterns = [
        "free", "offer", "loan", "credit card",
        "insurance", "investment", "policy",
        "cashback", "reward", "prize",
        "limited time", "emi", "interest",
        "लोन", "ऑफर", "फ्री", "पॉलिसी",
        "investment opportunity", "earn money",
        "work from home", "part time"
    ]

    # ✅ Important / Genuine patterns
    important_patterns = [
        "urgent", "emergency", "important",
        "asap", "immediately", "help",
        "जरूरी", "बहुत जरूरी", "इमरजेंसी",
        "turant", "abhi baat karni hai",
        "project", "meeting", "deadline",
        "interview", "college", "exam",
        "family matter", "ghar ka kaam"
    ]

    # 🤔 Normal / unclear patterns
    neutral_patterns = [
        "baat karni thi",
        "call back",
        "ek kaam tha",
        "time mile to call",
        "hello", "hi", "namaste"
    ]

    # 🔴 Spam check (highest priority)
    for p in spam_patterns:
        if p in text:
            return "REJECT"

    # 🟢 Important check
    for p in important_patterns:
        if p in text:
            return "FORWARD"

    # 🟡 Neutral
    for p in neutral_patterns:
        if p in text:
            return "ASK_MORE"

    # Default fallback
    return "ASK_MORE"