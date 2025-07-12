import pyttsx3

engine = pyttsx3.init()             # one global engine instance
engine.setProperty("rate", 175)     # speed (words per minute)
engine.setProperty("volume", 1.0)   # volume (0‑1)

def speak(text: str):
    """Convert the given text to speech and wait till done."""
    print(f"[Jarvis]: {text}")
    engine.say(text)
    engine.runAndWait()
