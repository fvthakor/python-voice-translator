# Real-Time Voice Translator 🎤🌐

A Python application that translates spoken language to any target language in real-time using speech recognition, translation, and text-to-speech technologies.

## Features

- 🎤 **Speech Recognition**: Captures and recognizes speech input in multiple languages
- 🔄 **Real-time Translation**: Translates between 10+ languages using Google Translate
- 🔊 **Text-to-Speech**: Converts translated text back to speech
- 🌍 **Multi-Language Support**: Hindi, English, Spanish, French, German, Chinese, Japanese, Arabic, Portuguese, Russian
- 🎯 **Interactive Menu**: Easy-to-use interface to select source and target languages
- 🔁 **Continuous Mode**: Keep translating without restarting the app
- 🚀 **Simple & Fast**: Command-line interface with clear instructions

## How It Works

1. Listens to spoken Hindi through your microphone
2. Converts Hindi speech to text using Google Speech Recognition
3. Translates Hindi text to English using Google Translate
4. Converts English text to speech using gTTS (Google Text-to-Speech)
5. Plays the translated audio output

## Prerequisites

- Python 3.7 or higher
- Working microphone
- Internet connection (required for translation and speech recognition APIs)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/real-time-voice-translater.git
cd real-time-voice-translater
```

### 2. Create a virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install PyAudio (if needed)

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

Or download the wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install:
```bash
pip install PyAudio‑0.2.11‑cp3x‑cp3xm‑win_amd64.whl
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-pyaudio
# or
sudo apt-get install portaudio19-dev
pip install pyaudio
```

## Usage

### Interactive App (Recommended)
Run the interactive version with language selection:
```bash
python app_interactive.py
```

**Features:**
1. Select the language you want to **SPEAK** (e.g., Hindi)
2. Select the language you want to **HEAR** (e.g., English)
3. Press ENTER to start speaking
4. The app will:
   - Display what you said in your language
   - Show the translation
   - Play the translated audio
5. Commands:
   - Press ENTER: Start new translation
   - Type `change`: Change language settings
   - Type `quit`: Exit the app

**Example Usage:**
- Speak: Hindi → Hear: English
- Speak: English → Hear: Spanish
- Speak: French → Hear: Japanese
- Any combination of 10+ languages!

### Basic App (Hindi to English only)
Run the basic version:
```bash
python app.py
```

1. When prompted with "🎤 Speak in Hindi...", speak clearly in Hindi
2. The app will display the recognized Hindi text
3. The English translation will be shown
4. The translated English audio will play automatically

## Dependencies

- **SpeechRecognition**: For converting speech to text
- **googletrans**: For translating Hindi to English
- **gTTS**: For converting English text to speech
- **playsound**: For playing the generated audio
- **PyAudio**: For microphone access

## Troubleshooting

### Microphone not detected
- Check if your microphone is properly connected
- Grant microphone permissions to your terminal/Python application
- Test your microphone with other applications

### PyAudio installation issues
- See the installation guide above for OS-specific instructions
- Make sure you have the correct Python version and architecture (32-bit vs 64-bit)

### Translation errors
- Ensure you have a stable internet connection
- The Google Translate API has rate limits; wait a moment if you get errors

### Audio playback issues
- Make sure your speakers/headphones are working
- Check system volume settings
- On Linux, you may need to install additional audio libraries:
  ```bash
  sudo apt-get install ffmpeg
  ```

## Future Enhancements

- [ ] Support for multiple language pairs
- [ ] GUI interface
- [ ] Save translation history
- [ ] Batch translation mode
- [ ] Custom voice selection
- [ ] Offline translation support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Speech Recognition API
- Google Translate API
- Google Text-to-Speech (gTTS)

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This application requires an active internet connection as it uses cloud-based APIs for speech recognition and translation.
