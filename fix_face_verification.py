"""
Fix active face verification to wait for fresh data
"""
import os

file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and fix the identity verification section
old_code = '''            # Active face verification for identity questions
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
                    print("[WARN] Face recognition check failed")'''

new_code = '''            # Active face verification for identity questions
            identity_keywords = ['who am i', 'my name', 'who i am', 'what is my name', 'whats my name']
            if any(keyword in command.lower() for keyword in identity_keywords):
                print("[INFO] Identity question detected - Verifying face...")
                try:
                    # Force immediate check of face recognition with retry
                    import time
                    for attempt in range(3):  # Try 3 times
                        response_data = requests.get("http://localhost:5000/current_greeting", timeout=2)
                        if response_data.status_code == 200:
                            data = response_data.json()
                            name = data.get("name", "")
                            if name and name != "Unknown":
                                self.current_user = name
                                print(f"[INFO] Face verified: {name}")
                                break
                            else:
                                if attempt < 2:  # Not last attempt
                                    time.sleep(0.5)  # Wait before retry
                                else:
                                    self.current_user = "Unknown"
                                    print("[INFO] No face detected after 3 attempts")
                except Exception as e:
                    print(f"[WARN] Face recognition check failed: {e}")'''

content = content.replace(old_code, new_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed active face verification!")
print("Now retries 3 times with 0.5s delay to ensure fresh face data")
