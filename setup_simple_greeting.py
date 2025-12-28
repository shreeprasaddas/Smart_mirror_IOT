import os

# Update Module with simplified styling
module_dir = os.path.join("MagicMirror", "modules", "MMM-FaceFeed")

js_content = """Module.register("MMM-FaceFeed", {
    defaults: {
        updateInterval: 1000,
        apiUrl: "http://localhost:5000/current_greeting"
    },

    start: function() {
        Log.info("Starting module: " + this.name);
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
                Log.info("Received data: " + JSON.stringify(data));
                if (data.name && data.greeting && data.timestamp !== self.lastUpdate) {
                    self.currentGreeting = data.greeting;
                    self.currentName = data.name;
                    self.lastUpdate = data.timestamp;
                    Log.info("Updating DOM with: " + data.greeting);
                    self.updateDom(300);
                }
            })
            .catch(err => {
                Log.error("Error fetching greeting: " + err);
            });
    },

    getDom: function() {
        var wrapper = document.createElement("div");
        wrapper.className = "greeting-container";
        
        if (this.currentGreeting) {
            var text = document.createElement("div");
            text.className = "greeting-text";
            text.innerHTML = this.currentGreeting;
            wrapper.appendChild(text);
        } else {
            var text = document.createElement("div");
            text.className = "greeting-text";
            text.innerHTML = "Waiting...";
            wrapper.appendChild(text);
        }
        
        return wrapper;
    },

    getStyles: function() {
        return ["MMM-FaceFeed.css"];
    }
});
"""

css_content = """.greeting-container {
    padding: 20px;
    background-color: white;
    border: 3px solid black;
    text-align: center;
}

.greeting-text {
    font-size: 48px;
    color: black;
    font-weight: bold;
    font-family: Arial, sans-serif;
}
"""

with open(os.path.join(module_dir, "MMM-FaceFeed.js"), "w") as f:
    f.write(js_content)
    print("Updated MMM-FaceFeed.js with simplified version")

with open(os.path.join(module_dir, "MMM-FaceFeed.css"), "w") as f:
    f.write(css_content)
    print("Updated MMM-FaceFeed.css with black and white styling")

print("Module updated - restart MagicMirror to see changes")
