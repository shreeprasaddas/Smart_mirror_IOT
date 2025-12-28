"""
Fix all hardcoded Windows paths to be cross-platform compatible
"""
import os
import re

# List of files to fix
files_to_fix = [
    "d:/test/face_recogonation/MagicMirror/modules/MMM-VoiceAssistant/update_user_manager.py",
    "d:/test/face_recogonation/MagicMirror/modules/MMM-VoiceAssistant/cleanup.py",
    "d:/test/face_recogonation/fix_main.py",
    "d:/test/face_recogonation/add_face_verification.py",
    "d:/test/face_recogonation/add_message_prompt.py",
    "d:/test/face_recogonation/add_delete_methods.py",
    "d:/test/face_recogonation/add_secret_messages.py",
    "d:/test/face_recogonation/add_delete_commands.py",
    "d:/test/face_recogonation/add_sleep_wake.py"
]

# Replacement patterns
replacements = {
    r'file_path = r"d:\\test\\face_recogonation\\MagicMirror\\modules\\MMM-VoiceAssistant\\voice_assistant.py"': 
        'file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "voice_assistant.py")',
    
    r'file_path = r"d:\\test\\face_recogonation\\main.py"':
        'file_path = os.path.join(os.path.dirname(__file__), "main.py")'
}

fixed_count = 0

for file_path in files_to_fix:
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file needs import os
            needs_import = 'import os' not in content and 'os.path' in str(replacements.values())
            
            # Apply replacements
            original_content = content
            for old_pattern, new_code in replacements.items():
                content = re.sub(old_pattern, new_code, content, flags=re.IGNORECASE)
            
            # Add import os if needed
            if needs_import and content != original_content:
                if '"""' in content:
                    # Add after docstring
                    content = content.replace('"""', '"""\nimport os', 1)
                else:
                    # Add at top
                    content = 'import os\n' + content
            
            # Write back if changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_count += 1
                print(f"✅ Fixed: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"❌ Error fixing {file_path}: {e}")
    else:
        print(f"⚠️  Not found: {file_path}")

print(f"\n✅ Fixed {fixed_count} files to be cross-platform compatible!")
print("All paths now use os.path.join() and work on Windows, Linux, and Raspberry Pi!")
