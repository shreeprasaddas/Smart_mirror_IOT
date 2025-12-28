import os

# Update Module styling
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
                if (data.name && data.greeting && data.timestamp !== self.lastUpdate) {
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
        wrapper.className = "greeting-container";
        
        if (this.currentGreeting) {
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

css_content = """.greeting-container {
    padding: 30px 50px;
    background-color: black;
    border: 3px solid white;
    text-align: center;
    border-radius: 10px;
}

.greeting-text {
    font-size: 48px;
    color: white;
    font-weight: bold;
    font-family: Arial, sans-serif;
}
"""

# Update config to position it in lower_third (center)
config_content = """/* Config with MMM-Remote-Control and MMM-FaceFeed */
let config = {
	address: "0.0.0.0", 
	port: 8080,
	basePath: "/", 
	ipWhitelist: [], 

	useHttps: false, 
	httpsPrivateKey: "", 
	httpsCertificate: "", 

	language: "en",
	locale: "en-US", 
	logLevel: ["INFO", "LOG", "WARN", "ERROR"],
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "US Holidays",
			position: "top_left",
			config: {
				calendars: [
					{
						symbol: "calendar-check",
						url: "https://ics.calendarlabs.com/76/mm3137/US_Holidays.ics"
					}
				]
			}
		},
		{
			module: "compliments",
			position: "lower_third"
		},
        {
            module: 'MMM-Remote-Control',
            config: {
                apiKey: '' 
            }
        },
        {
            module: 'MMM-FaceFeed',
            position: 'bottom_right',
            config: {
            }
        },
		{
			module: "weather",
			position: "top_right",
			config: {
				weatherProvider: "openmeteo",
				type: "current",
				lat: 40.776676,
				lon: -73.971321
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "New York Times",
						url: "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		},
	]
};

if (typeof module !== "undefined") { module.exports = config; }
"""

with open(os.path.join(module_dir, "MMM-FaceFeed.js"), "w") as f:
    f.write(js_content)
    print("Updated MMM-FaceFeed.js")

with open(os.path.join(module_dir, "MMM-FaceFeed.css"), "w") as f:
    f.write(css_content)
    print("Updated MMM-FaceFeed.css - black background, white text")

config_path = os.path.join("MagicMirror", "config", "config.js")
with open(config_path, "w") as f:
    f.write(config_content)
    print("Updated config.js - positioned at bottom_right")

print("\nDone! Restart MagicMirror to see: Black background, white text, bottom right corner")
