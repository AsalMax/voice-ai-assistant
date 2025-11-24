from gtts import gTTS
import os

def speak(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    os.system(f"start {filename}")  # Windows
