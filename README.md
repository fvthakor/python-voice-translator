# Real-Time Voice Translation Chat 🎤💬

A real-time multi-user chat application with voice translation capabilities. Users can speak in their native language and others hear it translated in their preferred language instantly!

## 🌟 Features

### Real-Time Chat Application (NEW! ⭐)
- 🌍 **Multi-User Support**: Multiple users can join and chat simultaneously
- 🔄 **Real-Time Translation**: Automatic translation between 10+ languages
- 🎤 **Voice Input**: Speak directly using your microphone
- 🔊 **Voice Output**: Hear translations spoken aloud automatically
- 💬 **Text Chat**: Type messages if you prefer
- 👥 **User Presence**: See who's online and what languages they speak
- ⌨️ **Typing Indicators**: Know when someone is typing
- 🎨 **Beautiful UI**: Modern, responsive web interface

### Standalone Voice Translator
- 🎯 **Interactive Menu**: Easy-to-use interface to select source and target languages
- 🔁 **Continuous Mode**: Keep translating without restarting
- 🚀 **Simple & Fast**: Command-line interface

### Supported Languages
🇮🇳 Hindi • 🇺🇸 English • 🇪🇸 Spanish • 🇫🇷 French • 🇩🇪 German • 🇨🇳 Chinese • 🇯🇵 Japanese • 🇸🇦 Arabic • 🇵🇹 Portuguese • 🇷🇺 Russian

## 🚀 Quick Start

### Installation

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

## 💬 Usage Options

### Option 1: Real-Time Chat (Multi-User) - RECOMMENDED! 🌟

**Start the server:**
```bash
python server.py
```

You'll see:
```
🌐 REAL-TIME VOICE TRANSLATION CHAT SERVER
🚀 Server starting on http://localhost:5000
💡 Open this URL in multiple browsers to test chat
```

**Open the chat:**
1. Open browser: `http://localhost:5000`
2. Enter your name
3. Select language to SPEAK (e.g., Hindi)
4. Select language to HEAR (e.g., English)
5. Click "Join Chat" 🚀

**Start chatting:**
- Click 🎤 Voice to speak
- Or type and click Send 📤
- Messages auto-translate for everyone!

**Multi-User Testing:**
- Open multiple browser tabs/windows
- Each user can select different languages
- Everyone sees translations in their language!

**Example Scenario:**
```
User A (Mumbai)  → Speaks: Hindi    → Hears: English
User B (New York) → Speaks: English  → Hears: Hindi
User C (Paris)    → Speaks: French   → Hears: English

All three can communicate naturally!
```

### Option 2: Interactive Voice Translator (Single User)

Run the interactive desktop app:
```bash
python app_interactive.py
```

**Features:**
1. Select language to SPEAK (e.g., Hindi)
2. Select language to HEAR (e.g., English)
3. Press ENTER to start speaking
4. Hear the translation automatically

### Option 3: Simple Translator (Hindi → English only)

Run the basic version:
```bash
python app.py
```

## 🛠️ Additional Setup

### Install PyAudio (if needed)

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

## 🌐 Network Access (For Real-Time Chat)

### Share with Local Network
To let others on your WiFi join the chat:

1. **Find your IP address:**
```bash
# Windows
ipconfig

# macOS/Linux
ifconfig
```

2. **Share the URL:** `http://YOUR_IP:5000`
   - Example: `http://192.168.1.100:5000`

### Public Internet Access (Advanced)
Use ngrok for internet access:
```bash
ngrok http 5000
```

## 📋 Dependencies

**For Chat Application:**
- **Flask**: Web framework
- **Flask-SocketIO**: WebSocket real-time communication
- **python-socketio**: Socket.IO server
- **SpeechRecognition**: Speech-to-text
- **googletrans**: Translation API
- **gTTS**: Text-to-speech
- **playsound**: Audio playback
- **PyAudio**: Microphone access

**Browser Requirements (for chat):**
- Chrome, Edge, or Safari (for Web Speech API)
- Microphone access permissions

## 🐛 Troubleshooting

### Real-Time Chat Issues

**Server won't start:**
- Make sure port 5000 is available
- Or change port in `server.py`

**Can't connect to chat:**
- Check if server is running
- Try `http://localhost:5000` first
- Check firewall settings

**Microphone not working in browser:**
- Grant microphone permissions
- Use Chrome or Edge browser
- Must use HTTPS or localhost

**Voice recognition not working:**
- Speak clearly and close to microphone
- Check browser console for errors
- Try refreshing the page

### Desktop App Issues

**Microphone not detected:**
- Check microphone connection
- Grant permissions to Python/Terminal
- Test microphone with other apps

**PyAudio installation issues:**
- See installation guide above
- Check Python version (32-bit vs 64-bit)

**Translation errors:**
- Check internet connection
- API has rate limits - wait if errors occur

**Audio playback issues:**
- Check speakers/headphones
- Verify system volume
- On Linux: `sudo apt-get install ffmpeg`

## 🎯 Browser Compatibility (Chat App)

| Browser | Voice Input | Voice Output | Real-Time Chat |
|---------|------------|--------------|----------------|
| Chrome  | ✅         | ✅           | ✅             |
| Edge    | ✅         | ✅           | ✅             |
| Safari  | ✅         | ✅           | ✅             |
| Firefox | ❌         | ✅           | ✅             |
| Opera   | ⚠️         | ✅           | ✅             |

## 🔮 Future Enhancements

**Chat Application:**
- [ ] Private rooms and direct messages
- [ ] Message history and search
- [ ] File/image sharing
- [ ] Video chat integration
- [ ] User authentication
- [ ] Message encryption
- [ ] Mobile app

**Voice Translator:**
- [ ] Offline translation support
- [ ] Custom voice selection
- [ ] Save translation history
- [ ] Batch translation mode

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Google Speech Recognition API
- Google Translate API
- Google Text-to-Speech (gTTS)
- Flask-SocketIO community
- Socket.IO community

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

**Built with ❤️ for breaking language barriers**

🌍 Connect people across languages in real-time!
