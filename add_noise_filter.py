"""
Add background noise filtering to listen method
"""
import os

file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the listen method to add noise filtering
old_listen = '''    def listen(self):
        """Listen for user speech and convert to text"""
        with self.microphone as source:
            # Print status for UI animation
            print("[LISTENING]")
            sys.stdout.flush()
            try:
                # 3s timeout, 100s phrase limit (Extended for long messages)
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=100)'''

new_listen = '''    def listen(self):
        """Listen for user speech and convert to text"""
        with self.microphone as source:
            # Adjust for ambient noise to filter background sounds
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            # Set higher energy threshold to ignore background noise
            self.recognizer.energy_threshold = 4000  # Higher = less sensitive
            self.recognizer.dynamic_energy_threshold = True  # Auto-adjust
            
            # Print status for UI animation
            print("[LISTENING]")
            sys.stdout.flush()
            try:
                # 3s timeout, 100s phrase limit (Extended for long messages)
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=100)'''

content = content.replace(old_listen, new_listen)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added background noise filtering!")
print("Settings:")
print("  - Ambient noise adjustment: 0.5 seconds")
print("  - Energy threshold: 4000 (filters background noise)")
print("  - Dynamic threshold: Enabled (auto-adjusts)")
