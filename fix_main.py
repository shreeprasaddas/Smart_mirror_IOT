"""
import os
Quick fix for main.py syntax error
"""
file_path = os.path.join(os.path.dirname(__file__), "main.py")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the syntax error by removing the misplaced try-except
content = content.replace(
    '''    t.daemon = True try:
                        requests.post("http://localhost:8080/api/notification/SHOW_ALERT", 
                                      json={"title": "Greeting", "message": greeting, "timer": 5000})
                    except Exception as e:
                        pass # Silent fail if MM is down
        
    t.start()''',
    '''    t.daemon = True
    t.start()'''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed syntax error in main.py!")
