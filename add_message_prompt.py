"""
import os
Add secret message commands to system prompt
"""
file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the productivity commands section and add secret message examples
old_text = '''2. Add to Routine:
User: "Add exercise to my morning routine"
Response: "Added exercise to your morning routine." [COMMAND] {"type": "ADD_ROUTINE", "time_of_day": "morning", "item": "Exercise"}

3. Control Mirror:'''

new_text = '''2. Add to Routine:
User: "Add exercise to my morning routine"
Response: "Added exercise to your morning routine." [COMMAND] {"type": "ADD_ROUTINE", "time_of_day": "morning", "item": "Exercise"}

3. Secret Message:
User: "Leave a message for John" or "Store a secret message for Unknown"
Response: "What's the message for John?" [COMMAND] {"type": "SAVE_MESSAGE", "to": "John", "message": "User will provide message"}
User: "Tell him to buy milk"
Response: "Message saved for John." [COMMAND] {"type": "SAVE_MESSAGE", "to": "John", "message": "Tell him to buy milk"}

4. Control Mirror:'''

content = content.replace(old_text, new_text)

# Also update the numbering for Control Mirror
content = content.replace('3. Control Mirror:', '4. Control Mirror:')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added secret message commands to system prompt!")
