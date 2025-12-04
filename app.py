import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

# Recognizer
r = sr.Recognizer()
translator = Translator()

print("\n🎤 Speak in Hindi...")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    # 1. Convert Hindi speech → Hindi text
    hindi_text = r.recognize_google(audio, language="hi-IN")
    print("🟢 Hindi Text:", hindi_text)

    # 2. Translate Hindi → English
    english_text = translator.translate(hindi_text, src="hi", dest="en").text
    print("🔵 English Translation:", english_text)

    # 3. Convert English text → English speech
    tts = gTTS(english_text, lang="en")
    filename = "english_output.mp3"
    tts.save(filename)

    print("\n🔊 Speaking English translation...")
    playsound.playsound(filename)

    os.remove(filename)

except Exception as e:
    print("❌ Error:", e)
