"""
import os
Add delete methods to UserManager
"""
file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the mark_messages_read method and add delete methods after it
delete_methods = '''
    
    def delete_reminder(self, reminder_id, user_name):
        """Delete a specific reminder by ID"""
        self._ensure_user(user_name)
        self.data["users"][user_name]["reminders"] = [
            r for r in self.data["users"][user_name]["reminders"] 
            if r.get("id") != reminder_id
        ]
        self.save_data()
        return "Reminder deleted."
    
    def delete_all_reminders(self, user_name):
        """Delete all reminders for a user"""
        self._ensure_user(user_name)
        self.data["users"][user_name]["reminders"] = []
        self.save_data()
        return "All reminders deleted."
    
    def delete_message(self, message_index, user_name):
        """Delete a specific message by index"""
        self._ensure_user(user_name)
        if "messages" in self.data["users"][user_name]:
            if 0 <= message_index < len(self.data["users"][user_name]["messages"]):
                self.data["users"][user_name]["messages"].pop(message_index)
                self.save_data()
                return "Message deleted."
        return "Message not found."
    
    def delete_all_messages(self, user_name):
        """Delete all messages for a user"""
        self._ensure_user(user_name)
        if "messages" in self.data["users"][user_name]:
            self.data["users"][user_name]["messages"] = []
            self.save_data()
        return "All messages deleted."
'''

# Insert after mark_messages_read method
insert_point = content.find('    def mark_messages_read(self, user_name):')
if insert_point != -1:
    # Find the end of mark_messages_read method
    next_method = content.find('\nclass MagicMirrorAssistant:', insert_point)
    if next_method != -1:
        content = content[:next_method] + delete_methods + content[next_method:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Added delete methods to UserManager!")
    else:
        print("❌ Could not find MagicMirrorAssistant class")
else:
    print("❌ Could not find mark_messages_read method")
