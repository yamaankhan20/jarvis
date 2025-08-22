from core.recognizer import listen
from core.tts import speak
from core.greetings import get_time_based_greeting
import datetime
import time

def listen_for_wakeword():
    """Detect wake word and handle one command at a time."""
    speak("Jarvis Voice Core initiated. Say 'Hey Jarvis' to wake me up.")

    while True:
        query = listen()

        if "hey" in query or "ok jarvis" in query:
            speak(get_time_based_greeting())
            speak("How can I help you?")

            command = listen()

            if "time" in command:
                now = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {now}")

            elif "hello" in command:
                speak("Hello! Nice to hear from you.")

            elif "exit" in command or "quit" in command:
                speak("Goodbye! Shutting down.")
                break

            else:
                speak("I heard you, but I don't know how to respond yet.")

            time.sleep(2)
            speak("Say 'Hey Jarvis' when you need me again.")