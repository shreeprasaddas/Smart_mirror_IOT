"""
import os
Add sleep/wake commands to system prompt
"""
file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the MONITOROFF example with sleep/wake examples
old_text = '''User: "Turn off screen"
Response: "Turning off screen." [COMMAND] {"type": "CONTROL_MM", "action": "MONITOROFF"}'''

new_text = '''User: "Turn off" or "Sleep" or "Shutdown"
Response: "Going to sleep mode." [COMMAND] {"type": "CONTROL_MM", "action": "HIDE", "module": "all"}
User: "Wake up" or "Mirror"
Response: "Waking up." [COMMAND] {"type": "CONTROL_MM", "action": "SHOW", "module": "all"}'''

content = content.replace(old_text, new_text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added sleep/wake commands to system prompt!")
