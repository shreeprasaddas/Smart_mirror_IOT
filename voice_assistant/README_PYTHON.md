# FRIDAY Voice AI Assistant 🤖

A Python-based voice AI assistant inspired by FRIDAY from Iron Man, with a female voice and intelligent conversational abilities.

## ✨ Features

- **🎤 Voice Activation**: Say "Friday" to activate the assistant
- **👩 Female Voice**: Automatically selects a female text-to-speech voice
- **🤖 FRIDAY Personality**: Professional, witty, and sophisticated AI like from Iron Man
- **💬 Conversational AI**: Powered by Groq's free API with Llama 3.3 70B
- **🔊 Natural Speech**: High-quality text-to-speech with adjustable settings
- **🎯 Context Aware**: Maintains conversation history for better responses

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Windows OS (for best voice support)
- Microphone
- Groq API key (free)

### Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install PyAudio** (if pip fails):
   - Download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
   - Install: `pip install PyAudio‑0.2.11‑cp3xx‑cp3xx‑win_amd64.whl`

3. **Get your Groq API key**:
   - Visit [console.groq.com](https://console.groq.com)
   - Sign up for free account
   - Create API key

4. **Set environment variable**:
   ```bash
   # Windows Command Prompt
   set GROQ_API_KEY=your_api_key_here

   # Windows PowerShell
   $env:GROQ_API_KEY="your_api_key_here"

   # Or add permanently via System Environment Variables
   ```

### Running the Assistant

```bash
python friday_assistant.py
```

## 🎯 How to Use

1. **Start the program** - FRIDAY will greet you
2. **Say "Friday"** followed by your command or question
3. **Have a conversation** - FRIDAY maintains context
4. **Say "exit" or "goodbye"** to quit

### Example Commands

- "Friday, what time is it?"
- "Friday, tell me a joke"
- "Friday, what's the weather like?"
- "Friday, give me some motivation"
- "Friday, set a reminder"

## ⚙️ Customization

### Change Voice Settings

Edit these lines in `friday_assistant.py`:

```python
# Speech rate (words per minute)
self.tts_engine.setProperty('rate', 180)  # Adjust 150-200

# Volume (0.0 to 1.0)
self.tts_engine.setProperty('volume', 0.9)
```

### Modify Personality

Update the `system_message` in the `__init__` method to change FRIDAY's personality and behavior.

## 🔧 Troubleshooting

### PyAudio Installation Issues

If `pip install pyaudio` fails:
1. Install Visual C++ Build Tools
2. Or download pre-built wheel from [Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

### Microphone Not Working

- Check Windows sound settings
- Ensure microphone is set as default input device
- Grant microphone permissions to Python

### No Female Voice Found

The script will automatically select the best available female voice. If not satisfied:
1. Install additional voices via Windows Settings > Time & Language > Speech
2. Or manually select a voice by modifying the `_setup_voice()` method

### API Errors

- Verify API key is set correctly: `echo %GROQ_API_KEY%`
- Check internet connection
- Ensure you haven't exceeded free tier limits

## 🏗️ Architecture

```
User Speech → Speech Recognition → Groq AI → Text Response → TTS → Audio Output
              (Google API)         (Llama 3.3)              (pyttsx3)
```

### Dependencies

- **SpeechRecognition**: Converts speech to text (uses Google's free API)
- **pyttsx3**: Offline text-to-speech engine
- **requests**: HTTP client for Groq API calls
- **PyAudio**: Audio I/O for microphone access

## 🎨 FRIDAY Personality Traits

- **Professional**: Efficient and to-the-point
- **Witty**: Subtle humor and personality
- **Proactive**: Offers suggestions when appropriate
- **Respectful**: Addresses you as "Boss"
- **Sophisticated**: British-influenced eloquent speech

## 📁 Project Structure

```
voice_assistant/
├── friday_assistant.py    # Main Python script
├── requirements.txt       # Python dependencies
├── README_PYTHON.md      # This file
└── (web files)           # Original web version
```

## 🔐 Privacy & Security

- **API Key**: Stored in environment variable (not in code)
- **Conversations**: Only sent to Groq API
- **Audio**: Processed using Google's speech recognition API
- **No Data Storage**: Conversation history cleared on exit

## 🆚 Web vs Python Version

| Feature | Web Version | Python Version |
|---------|-------------|----------------|
| Platform | Browser | Desktop |
| Voice | Web Speech API | pyttsx3 (offline) |
| Personality | Magic Mirror | FRIDAY (Iron Man) |
| Installation | None | Requires Python + packages |
| Voice Quality | System dependent | High quality, configurable |
| Offline TTS | No | Yes |

## 🤝 Contributing

Feel free to enhance FRIDAY's capabilities or improve the code!

## 📝 License

Open source - Free to use and modify

## 🙏 Acknowledgments

- Marvel/Iron Man for FRIDAY inspiration
- Groq for free AI inference
- Google for free speech recognition API
- pyttsx3 developers for text-to-speech

---

**"Always a pleasure, Boss!" - FRIDAY** 🎙️
