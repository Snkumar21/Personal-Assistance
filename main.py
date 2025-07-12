"""
Phase ‑ 1 loop: wake, listen, act on very small set of intents,
then respond by voice.
"""

from datetime import datetime
import sys
from speech.listener import listen
from speech.speaker import speak

WAKE_WORDS = ("hey jarvis", "ok jarvis", "jarvis", "wake up jarvis", "It's time to play jarvis")

def is_wake_word(text: str | None) -> bool:
    return text is not None and any(word in text for word in WAKE_WORDS)

def handle_intent(text: str | None):
    """
    Very tiny intent handler:
    time → say the time
    exit/quit/stop → quit program
    """
    if text is None:
        speak("I didn't catch that. Could you say it again?")
        return

    if "time" in text:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif any(word in text for word in ("exit", "quit", "stop")):
        speak("Goodbye!")
        sys.exit(0)
    else:
        speak("Sorry, I don't have a skill for that yet.")

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