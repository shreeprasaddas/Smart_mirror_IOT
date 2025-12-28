"""
import os
Add active face verification for identity questions
"""
file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section where we process commands and add face verification
old_code = '''            # Optimize: Skip API for very simple acknowledgments or noise
            simple_words = ['yes', 'no', 'ok', 'okay', 'yeah', 'nah', 'yep', 'nope', 'uh', 'um', 'hmm']
            if command.lower() in simple_words:
                print(f"[INFO] Simple acknowledgment detected, skipping API call")
                continue
            
            # Get AI response and speak it
            response = self.get_ai_response(command)
            self.speak(response)'''

new_code = '''            # Optimize: Skip API for very simple acknowledgments or noise
            simple_words = ['yes', 'no', 'ok', 'okay', 'yeah', 'nah', 'yep', 'nope', 'uh', 'um', 'hmm']
            if command.lower() in simple_words:
                print(f"[INFO] Simple acknowledgment detected, skipping API call")
                continue
            
            # Active face verification for identity questions
            identity_keywords = ['who am i', 'my name', 'who i am', 'what is my name', 'whats my name']
            if any(keyword in command.lower() for keyword in identity_keywords):
                print("[INFO] Identity question detected - Checking face recognition...")
                try:
                    # Force immediate check of face recognition
                    response_data = requests.get("http://localhost:5000/current_greeting", timeout=1)
                    if response_data.status_code == 200:
                        data = response_data.json()
                        name = data.get("name", "")
                        if name and name != "Unknown":
                            self.current_user = name
                            print(f"[INFO] Face verified: {name}")
                        else:
                            self.current_user = "Unknown"
                            print("[INFO] No face detected")
                except:
                    print("[WARN] Face recognition check failed")
            
            # Get AI response and speak it
            response = self.get_ai_response(command)
            self.speak(response)'''

content = content.replace(old_code, new_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added active face verification for identity questions!")
