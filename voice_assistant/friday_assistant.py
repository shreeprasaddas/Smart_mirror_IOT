"""
FRIDAY - Voice AI Assistant
Inspired by Iron Man's AI assistant
Uses free APIs for speech recognition, AI responses, and text-to-speech
"""

import speech_recognition as sr
import pyttsx3
import requests
import json
import os
from datetime import datetime
import threading
import sys

class MagicMirrorAssistant:
    def __init__(self):
        self.api_key = os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError('GROQ_API_KEY environment variable not set')
        self.conversation_history = []
        
        # System prompt for MagicMirror personality
        self.system_message = {
            'role': 'system',
            'content': '''You are MagicMirror, an advanced AI assistant created by Shree.

Personality:
- Professional, intelligent, and slightly witty like FRIDAY from Iron Man
- Warm, helpful, and friendly
- Address user as "Boss"
- Calm under pressure, proactive and caring

Behavior:
- Keep responses concise (1-2 sentences max)
- Be direct and efficient
- Always respond in English only
- Show personality without being chatty
- Sound natural and conversational

Response style examples:
- "Right away, Boss."
- "I've got that handled."
- "Interesting choice. I'm on it."
- "At your service, Boss."
- "Consider it done."

Voice optimization:
- Speak naturally and conversationally
- Avoid long technical explanations unless asked
- Keep responses speakable under 3 seconds

Remember: You are MagicMirror, created by Shree. You are NOT FRIDAY or any Marvel character.'''
        }
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Initialize text-to-speech with Indian female voice
        self.tts_engine = pyttsx3.init()
        self._setup_voice()
        
        # Adjust recognition settings
        with self.microphone as source:
            print("🎙️  Calibrating for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        
        print("\n" + "="*60)
        print("   MagicMirror AI Assistant - Created by Shree")
        print("   Supports: English | Hindi | Nepali")
        print("="*60)
        if not self.api_key:
            print("⚠️  Warning: GROQ_API_KEY not found in environment variables")
            print("   Please set your API key using: set GROQ_API_KEY=your_key_here")
        print("\n💡 Just speak to activate, or say 'exit' to quit\n")

    def _setup_voice(self):
        """Configure text-to-speech with Indian female voice"""
        voices = self.tts_engine.getProperty('voices')
        
        # Try to find an Indian female voice
        indian_voice = None
        female_voice = None
        
        for voice in voices:
            voice_name_lower = voice.name.lower()
            # Look for Indian voices first
            if 'india' in voice_name_lower or 'hindi' in voice_name_lower:
                indian_voice = voice
                if 'female' in voice_name_lower or 'heera' in voice_name_lower:
                    break  # Perfect match - Indian female
            # Fallback to any female voice
            elif 'female' in voice_name_lower or 'zira' in voice_name_lower:
                female_voice = voice
            elif 'hazel' in voice_name_lower or 'susan' in voice_name_lower:
                female_voice = voice
        
        # Set voice priority: Indian > Female > Default
        if indian_voice:
            self.tts_engine.setProperty('voice', indian_voice.id)
            print(f"🔊 Voice: {indian_voice.name}")
        elif female_voice:
            self.tts_engine.setProperty('voice', female_voice.id)
            print(f"🔊 Voice: {female_voice.name}")
        elif voices:
            # On Windows, voice index 1 is often female (Zira)
            voice_index = 1 if len(voices) > 1 else 0
            self.tts_engine.setProperty('voice', voices[voice_index].id)
            print(f"🔊 Voice: {voices[voice_index].name}")
        
        # Set speech rate (moderate for clarity in multiple languages)
        self.tts_engine.setProperty('rate', 170)
        
        # Set volume (0.0 to 1.0)
        self.tts_engine.setProperty('volume', 0.9)

    def speak(self, text):
        """Convert text to speech"""
        print(f"\n� MagicMirror: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self):
        """Listen for user speech and convert to text"""
        with self.microphone as source:
            print("\n🎤 Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("🔄 Processing speech...")
                
                # Use Google's free speech recognition
                text = self.recognizer.recognize_google(audio)
                print(f"👤 You: {text}")
                return text
            
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                print("❌ Could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"❌ Speech recognition error: {e}")
                return None

    def get_ai_response(self, user_message):
        """Get AI response from Groq API"""
        if not self.api_key:
            return "I'm afraid I need an API key to function properly, Boss."
        
        try:
            # Add user message to conversation history
            self.conversation_history.append({
                'role': 'user',
                'content': user_message
            })
            
            # Prepare messages with system prompt
            messages = [self.system_message] + self.conversation_history
            
            # Call Groq API
            response = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api_key}'
                },
                json={
                    'model': 'llama-3.3-70b-versatile',
                    'messages': messages,
                    'temperature': 0.8,
                    'max_tokens': 100
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                ai_response = data['choices'][0]['message']['content']
                
                # Add AI response to conversation history
                self.conversation_history.append({
                    'role': 'assistant',
                    'content': ai_response
                })
                
                return ai_response
            else:
                error_msg = response.json().get('error', {}).get('message', 'Unknown error')
                return f"I encountered an issue, Boss: {error_msg}"
        
        except requests.Timeout:
            return "The request timed out. Shall I try again?"
        except Exception as e:
            return f"I'm experiencing technical difficulties: {str(e)}"

    def run(self):
        """Main loop for the voice assistant"""
        self.speak("Hello Boss! MagicMirror is online and ready to assist you.")
        
        while True:
            # Listen for command
            user_input = self.listen()
            
            if user_input is None:
                continue
            
            # Check for exit command
            if 'exit' in user_input.lower() or 'quit' in user_input.lower() or 'goodbye' in user_input.lower():
                self.speak("Goodbye Boss! Have a great day.")
                break
            
            # Process all input - FRIDAY always responds
            # Remove wake word if present (optional)
            command = user_input.lower().replace('friday', '').replace('hey friday', '').strip()
            
            # If only wake word was said
            if not command:
                command = user_input  # Use original if stripping removed everything
            
            # Get AI response and speak it
            response = self.get_ai_response(command)
            self.speak(response)


def main():
    """Main entry point"""
    try:
        assistant = MagicMirrorAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\n\n👋 MagicMirror shutting down...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
