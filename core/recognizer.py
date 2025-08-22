import speech_recognition as sr
import winsound

recognizer = sr.Recognizer()

def get_working_microphone():
    """Auto-detect a working microphone index by testing each one."""
    mic_list = sr.Microphone.list_microphone_names()
    for index, name in enumerate(mic_list):
        try:
            with sr.Microphone(device_index=index) as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                if audio and len(audio.get_wav_data()) > 0:
                    return index
        except Exception as e:
            continue

    print("No working microphone found. Defaulting to 0.")
    return 0


MIC_INDEX = get_working_microphone()

def listen():
    """Listen from microphone and return recognized text."""
    with sr.Microphone(device_index=MIC_INDEX) as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        print("Listening now...")

        try:
            audio = recognizer.listen(source)
            print("Got audio, processing...")
        except sr.WaitTimeoutError:
            print("Timeout: no speech detected")
            return ""

    try:
        query = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"API error: {e}")
        return "error"
