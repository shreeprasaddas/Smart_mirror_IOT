"""
import os
Add delete commands to system prompt and command processing
"""
file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add DELETE_REMINDER and DELETE_MESSAGE to command processing
old_processing = '''                    elif c_type == "READ_MESSAGES":
                        # Mark messages as read
                        self.user_manager.mark_messages_read(self.current_user)
                        print(f"[ACTION] Messages marked as read for {self.current_user}")'''

new_processing = '''                    elif c_type == "READ_MESSAGES":
                        # Mark messages as read
                        self.user_manager.mark_messages_read(self.current_user)
                        print(f"[ACTION] Messages marked as read for {self.current_user}")
                    elif c_type == "DELETE_REMINDER":
                        # Delete reminder
                        self.user_manager.delete_all_reminders(self.current_user)
                        print(f"[ACTION] Deleted all reminders for {self.current_user}")
                    elif c_type == "DELETE_MESSAGE":
                        # Delete messages
                        self.user_manager.delete_all_messages(self.current_user)
                        print(f"[ACTION] Deleted all messages for {self.current_user}")'''

content = content.replace(old_processing, new_processing)

# Add delete examples to system prompt
old_prompt = '''User: "Tell him to buy milk"
Response: "Message saved for John." [COMMAND] {"type": "SAVE_MESSAGE", "to": "John", "message": "Tell him to buy milk"}

4. Control Mirror:'''

new_prompt = '''User: "Tell him to buy milk"
Response: "Message saved for John." [COMMAND] {"type": "SAVE_MESSAGE", "to": "John", "message": "Tell him to buy milk"}

When showing reminders or messages, ALWAYS ask if user wants to delete them:
User: "Any reminders?"
Response: "You have a reminder at 18:00 for coffee. Would you like me to delete it?"
User: "Yes" or "Delete it"
Response: "Reminder deleted." [COMMAND] {"type": "DELETE_REMINDER"}

User: "Show my messages"
Response: "You have a message from John: Buy milk. Would you like me to delete it?"
User: "Yes"
Response: "Message deleted." [COMMAND] {"type": "DELETE_MESSAGE"}

4. Control Mirror:'''

content = content.replace(old_prompt, new_prompt)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added delete functionality to system prompt and command processing!")
