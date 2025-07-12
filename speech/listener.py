import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(lang: str = "en-IN") -> str | None:
    """
    Listens from the default microphone and returns the recognised text.
    Returns None if nothing was understood.
    """
    with sr.Microphone() as source:
        print("[Listening...]")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source, phrase_time_limit=6)

    try:
        text = recognizer.recognize_google(audio, language=lang)
        print(f"[User]: {text}")
        return text.lower()
    except sr.UnknownValueError:
        # speech was unintelligible
        return None
    except sr.RequestError as e:
        print(f"[Error] Speech service error: {e}")
        return None
