def hindi_reply(decision: str) -> str:
    if decision == "FORWARD":
        return (
            "Dhanyavaad. "
            "Aapka call ab connect kiya ja raha hai. "
            "Kripya line par bane rahein."
        )
    elif decision == "REJECT":
        return (
            "Kshama kijiye. "
            "Is samay hum aapka call connect nahi kar paayenge."
        )
    else:
        return (
            "Kripya apna kaam. "
            "Thoda aur spasht batayein."
        )