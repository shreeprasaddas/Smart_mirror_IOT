import os

# 1. Update Module JS
module_dir = os.path.join("MagicMirror", "modules", "MMM-FaceFeed")

js_content = """Module.register("MMM-FaceFeed", {
    defaults: {
        updateInterval: 1000,
        apiUrl: "http://localhost:5000/current_greeting"
    },

    start: function() {
        this.currentGreeting = "";
        this.currentName = "";
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
                if (data.name && data.name !== "Unknown" && data.greeting) {
                    if (self.currentName !== data.name) {
                        self.currentGreeting = data.greeting;
                        self.currentName = data.name;
                        self.updateDom(500);
                    }
                }
            })
            .catch(err => {});
    },

    getDom: function() {
        var wrapper = document.createElement("div");
        wrapper.className = "face-greeting-wrapper";
        
        if (this.currentName && this.currentName !== "Unknown") {
            var greetingDiv = document.createElement("div");
            greetingDiv.className = "face-greeting-text";
            greetingDiv.innerHTML = this.currentGreeting;
            wrapper.appendChild(greetingDiv);
        }
        
        return wrapper;
    },

    getStyles: function() {
        return ["MMM-FaceFeed.css"];
    }
});
"""

css_content = """.face-greeting-wrapper {
    text-align: center;
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(135deg, rgba(30, 144, 255, 0.2), rgba(138, 43, 226, 0.2));
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    min-width: 300px;
    animation: fadeInUp 0.6s ease-out;
}

.face-greeting-text {
    font-size: 32px;
    font-weight: bold;
    color: #ffffff;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes glow {
    from {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5),
                     0 0 10px rgba(255, 255, 255, 0.3);
    }
    to {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5),
                     0 0 20px rgba(255, 255, 255, 0.6),
                     0 0 30px rgba(138, 43, 226, 0.4);
    }
}
"""

with open(os.path.join(module_dir, "MMM-FaceFeed.js"), "w") as f:
    f.write(js_content)
    print("Updated MMM-FaceFeed.js")

with open(os.path.join(module_dir, "MMM-FaceFeed.css"), "w") as f:
    f.write(css_content)
    print("Created MMM-FaceFeed.css")

print("Module updated successfully!")
