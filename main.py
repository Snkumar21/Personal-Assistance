from speech.listener import listen
from speech.speaker import speak
from tasks.apps import open_notepad, open_chrome, play_music
from tasks.internet import search_google, get_public_ip
from tasks.tools import take_screenshot, get_joke
from speech.speaker import speak
from datetime import datetime
import sys

WAKE_WORDS = ("hey jarvis", "ok jarvis", "jarvis", "wake up jarvis", "It's time to play jarvis")

def is_wake_word(text: str | None) -> bool:
    return text is not None and any(word in text for word in WAKE_WORDS)

def handle_intent(text: str | None):
    if text is None:
        speak("I didn't catch that. Please repeat.")
        return

    if "time" in text:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "notepad" in text:
        speak("Opening Notepad.")
        open_notepad()

    elif "chrome" in text:
        speak("Launching Chrome.")
        open_chrome()

    elif "play music" in text:
        speak("Playing your music.")
        play_music()

    elif "search" in text and "google" in text:
        query = text.replace("search", "").replace("google", "").strip()
        speak(f"Searching Google for {query}")
        search_google(query)

    elif "screenshot" in text:
        speak("Taking screenshot.")
        take_screenshot()

    elif "ip address" in text:
        ip = get_public_ip()
        speak(f"Your IP address is {ip}")

    elif "joke" in text:
        joke = get_joke()
        speak(joke)

    elif any(word in text for word in ("exit", "quit", "stop")):
        speak("Goodbye!")
        sys.exit(0)

    else:
        speak("Sorry, I don't know how to do that yet.")


def main():
    speak("Jarvis online.")
    while True:
        text = listen()
        if is_wake_word(text):
            speak("Yes?")
            command = listen()
            handle_intent(command)

if __name__ == "__main__":
    main()