import pyttsx3

def speak(text: str):
    """
    Say `text` aloud and return only when finished.
    Creates a fresh engine each call (safe but still fast).
    """
    print(f"[Jarvis]: {text}")

    engine = pyttsx3.init('sapi5')      # ← Windows driver
    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()