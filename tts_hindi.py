import subprocess

def speak_hindi(text: str):
    # Try best available clear voices (fallback order)
    voices = ["Lekha", "Rishi", "Samantha", "Alex"]

    for voice in voices:
        try:
            subprocess.run(
                ["say", "-v", voice, "-r", "165", text],
                check=True
            )
            break
        except Exception:
            continue