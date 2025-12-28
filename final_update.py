import os

module_dir = os.path.join("MagicMirror", "modules", "MMM-FaceFeed")

# Update JavaScript to hide when no face
js_content = """Module.register("MMM-FaceFeed", {
    defaults: {
        updateInterval: 1000,
        apiUrl: "http://localhost:5000/current_greeting"
    },

    start: function() {
        this.currentGreeting = "";
        this.currentName = "";
        this.lastUpdate = 0;
        this.scheduleUpdate();
    },

    scheduleUpdate: function() {
        var self = this;
        setInterval(function() {
            self.updateGreeting();
        }, this.config.updateInterval);
    },

    updateGreeting: function() {
        var self = this;
        fetch(this.config.apiUrl)
            .then(response => response.json())
            .then(data => {
                // Hide if no name or Unknown
                if (!data.name || data.name === "Unknown" || data.name === "") {
                    if (self.currentGreeting !== "") {
                        self.currentGreeting = "";
                        self.currentName = "";
                        self.updateDom(300);
                    }
                } else if (data.greeting && data.timestamp !== self.lastUpdate) {
                    self.currentGreeting = data.greeting;
                    self.currentName = data.name;
                    self.lastUpdate = data.timestamp;
                    self.updateDom(300);
                }
            })
            .catch(err => {});
    },

    getDom: function() {
        var wrapper = document.createElement("div");
        
        if (this.currentGreeting && this.currentName) {
            wrapper.className = "greeting-container";
            var text = document.createElement("div");
            text.className = "greeting-text";
            text.innerHTML = this.currentGreeting;
            wrapper.appendChild(text);
        }
        
        return wrapper;
    },

    getStyles: function() {
        return ["MMM-FaceFeed.css"];
    }
});
"""

# Transparent background CSS
css_content = """.greeting-container {
    padding: 30px 50px;
    background-color: transparent;
    border: 3px solid white;
    text-align: center;
    border-radius: 10px;
}

.greeting-text {
    font-size: 48px;
    color: white;
    font-weight: normal;
    font-family: Arial, sans-serif;
}
"""

with open(os.path.join(module_dir, "MMM-FaceFeed.js"), "w") as f:
    f.write(js_content)
    print("✓ Updated JavaScript - auto-hide when no face")

with open(os.path.join(module_dir, "MMM-FaceFeed.css"), "w") as f:
    f.write(css_content)
    print("✓ Updated CSS - transparent background")

print("\nRestart MagicMirror to see:")
print("  • Transparent background")
print("  • Auto-hide when no one is detected")
