from stt.stt import transcribe
from tts.tts import speak

def run_assistant():
    speak("Good morning! I'm ready. Please say your plan.")
    text = transcribe("audio.wav")
    print("You said:", text)
    speak("Got it! I will add this to your calendar.")
