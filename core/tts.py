import pyttsx3

def speak(text: str):
    print(f"Jarvis says: {text}")   # debug print

    engine = pyttsx3.init()

    # Female voice (if available)
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 175)  # speaking speed
    engine.say(text)
    engine.runAndWait()
    engine.stop()   # release resources
