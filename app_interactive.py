import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os
import time

class VoiceTranslator:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        
        # Language configurations
        self.languages = {
            '1': {'name': 'Hindi', 'code': 'hi', 'speech_code': 'hi-IN'},
            '2': {'name': 'English', 'code': 'en', 'speech_code': 'en-US'},
            '3': {'name': 'Spanish', 'code': 'es', 'speech_code': 'es-ES'},
            '4': {'name': 'French', 'code': 'fr', 'speech_code': 'fr-FR'},
            '5': {'name': 'German', 'code': 'de', 'speech_code': 'de-DE'},
            '6': {'name': 'Chinese', 'code': 'zh-cn', 'speech_code': 'zh-CN'},
            '7': {'name': 'Japanese', 'code': 'ja', 'speech_code': 'ja-JP'},
            '8': {'name': 'Arabic', 'code': 'ar', 'speech_code': 'ar-SA'},
            '9': {'name': 'Portuguese', 'code': 'pt', 'speech_code': 'pt-PT'},
            '10': {'name': 'Russian', 'code': 'ru', 'speech_code': 'ru-RU'}
        }
        
        self.source_lang = None
        self.target_lang = None
    
    def display_header(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("🌐 REAL-TIME VOICE TRANSLATOR 🎤".center(60))
        print("=" * 60)
        print()
    
    def display_languages(self):
        print("\n📋 Available Languages:")
        print("-" * 40)
        for key, lang in self.languages.items():
            print(f"  {key}. {lang['name']}")
        print("-" * 40)
    
    def select_language(self, prompt):
        while True:
            self.display_languages()
            choice = input(f"\n{prompt}: ").strip()
            if choice in self.languages:
                return self.languages[choice]
            else:
                print("❌ Invalid choice! Please try again.\n")
                time.sleep(1)
    
    def setup_languages(self):
        self.display_header()
        print("🎯 SETUP YOUR TRANSLATION\n")
        
        print("Select the language you will SPEAK:")
        self.source_lang = self.select_language("Enter your choice (1-10)")
        
        self.display_header()
        print("🎯 SETUP YOUR TRANSLATION\n")
        print(f"✅ Speaking Language: {self.source_lang['name']}\n")
        
        print("Select the language you want to HEAR (translate to):")
        self.target_lang = self.select_language("Enter your choice (1-10)")
        
        if self.source_lang['code'] == self.target_lang['code']:
            print("\n⚠️  Warning: Source and target languages are the same!")
            time.sleep(2)
    
    def display_session_info(self):
        self.display_header()
        print("🔄 TRANSLATION SESSION")
        print("-" * 60)
        print(f"  🎤 Speak in: {self.source_lang['name']}")
        print(f"  🔊 Hear in:  {self.target_lang['name']}")
        print("-" * 60)
        print("\n💡 Commands:")
        print("  - Press ENTER to start speaking")
        print("  - Type 'change' to change languages")
        print("  - Type 'quit' to exit")
        print("-" * 60)
    
    def listen_and_translate(self):
        try:
            with sr.Microphone() as source:
                print(f"\n🎤 Listening... Speak in {self.source_lang['name']}...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
            
            print("🔄 Processing...")
            
            # Step 1: Convert speech to text
            source_text = self.recognizer.recognize_google(
                audio, 
                language=self.source_lang['speech_code']
            )
            print(f"\n📝 You said ({self.source_lang['name']}): {source_text}")
            
            # Step 2: Translate text
            if self.source_lang['code'] != self.target_lang['code']:
                translation = self.translator.translate(
                    source_text, 
                    src=self.source_lang['code'], 
                    dest=self.target_lang['code']
                )
                target_text = translation.text
            else:
                target_text = source_text
            
            print(f"🌐 Translation ({self.target_lang['name']}): {target_text}")
            
            # Step 3: Convert translated text to speech
            tts = gTTS(target_text, lang=self.target_lang['code'])
            filename = "translation_output.mp3"
            tts.save(filename)
            
            print("🔊 Playing translation...\n")
            playsound.playsound(filename)
            
            # Clean up
            if os.path.exists(filename):
                os.remove(filename)
            
            print("✅ Translation complete!")
            
        except sr.WaitTimeoutError:
            print("⏱️  No speech detected. Please try again.")
        except sr.UnknownValueError:
            print("❌ Could not understand the audio. Please speak clearly.")
        except sr.RequestError as e:
            print(f"❌ Speech recognition error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def run(self):
        self.display_header()
        print("Welcome to Real-Time Voice Translator! 🎉\n")
        time.sleep(1)
        
        # Initial setup
        self.setup_languages()
        
        # Main loop
        while True:
            self.display_session_info()
            user_input = input("\n➤ Press ENTER to speak (or type command): ").strip().lower()
            
            if user_input == 'quit' or user_input == 'exit':
                print("\n👋 Thank you for using Voice Translator! Goodbye!\n")
                break
            elif user_input == 'change':
                self.setup_languages()
            else:
                self.listen_and_translate()
                input("\nPress ENTER to continue...")

if __name__ == "__main__":
    try:
        app = VoiceTranslator()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
