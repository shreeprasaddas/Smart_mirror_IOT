"""
import os
Add secret message functionality to UserManager
"""
file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of get_routine method and add secret message methods
secret_message_methods = '''
    
    def add_secret_message(self, from_user, to_user, message):
        """Add a secret message from one user to another"""
        self._ensure_user(to_user)
        if "messages" not in self.data["users"][to_user]:
            self.data["users"][to_user]["messages"] = []
        
        self.data["users"][to_user]["messages"].append({
            "from": from_user,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "read": False
        })
        self.save_data()
        return f"Secret message saved for {to_user}."
    
    def get_unread_messages(self, user_name):
        """Get unread messages for a user"""
        self._ensure_user(user_name)
        if "messages" not in self.data["users"][user_name]:
            return []
        return [m for m in self.data["users"][user_name]["messages"] if not m.get("read", False)]
    
    def mark_messages_read(self, user_name):
        """Mark all messages as read for a user"""
        self._ensure_user(user_name)
        if "messages" in self.data["users"][user_name]:
            for msg in self.data["users"][user_name]["messages"]:
                msg["read"] = True
            self.save_data()
'''

# Insert after the get_routine method
insert_point = content.find('    def get_routine(self, time_of_day, user_name="Unknown"):')
if insert_point != -1:
    # Find the end of get_routine method (next class definition)
    next_class = content.find('\nclass MagicMirrorAssistant:', insert_point)
    if next_class != -1:
        content = content[:next_class] + secret_message_methods + content[next_class:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Added secret message methods to UserManager!")
    else:
        print("❌ Could not find MagicMirrorAssistant class")
else:
    print("❌ Could not find get_routine method")
