"""
Fix JSON parsing in node_helper.js
"""
import os

file_path = os.path.join(os.path.dirname(__file__), "MagicMirror", "modules", "MMM-VoiceAssistant", "node_helper.js")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the JSON parsing to be more robust
old_code = '''                // Check for Control Commands
                if (message.includes("[COMMAND]")) {
                    try {
                        // Extract JSON from "[COMMAND] { ... }"
                        const jsonStr = message.match(/\\[COMMAND\\]\\s*({.*})/)[1];
                        const payload = JSON.parse(jsonStr);
                        self.sendSocketNotification("CONTROL_CMD", payload);
                        console.log("[NODE] Sent Control Command:", payload);
                    } catch (e) {
                        console.error("[NODE] Failed to parse command:", e);'''

new_code = '''                // Check for Control Commands
                if (message.includes("[COMMAND]")) {
                    try {
                        // Extract JSON from "[COMMAND] { ... }" - more robust
                        const match = message.match(/\\[COMMAND\\]\\s*(\\{[^}]*\\})/);
                        if (match && match[1]) {
                            const jsonStr = match[1];
                            const payload = JSON.parse(jsonStr);
                            self.sendSocketNotification("CONTROL_CMD", payload);
                            console.log("[NODE] Sent Control Command:", payload);
                        }
                    } catch (e) {
                        console.error("[NODE] Failed to parse command:", e.message);
                        // Don't crash - just log and continue'''

content = content.replace(old_code, new_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed JSON parsing in node_helper.js!")
print("Now handles malformed JSON gracefully")
