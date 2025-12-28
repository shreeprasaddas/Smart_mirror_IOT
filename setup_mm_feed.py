import os

# 1. Create Module JS
module_dir = os.path.join("MagicMirror", "modules", "MMM-FaceFeed")
if not os.path.exists(module_dir):
    os.makedirs(module_dir)

js_content = """Module.register("MMM-FaceFeed", {
    defaults: {
        url: "http://localhost:5000/video_feed",
        width: "300px",
        height: "auto"
    },

    getDom: function() {
        var wrapper = document.createElement("div");
        var title = document.createElement("div");
        title.innerHTML = "Face Recognition Live";
        title.style.fontSize = "small";
        title.style.marginBottom = "5px";
        wrapper.appendChild(title);

        var img = document.createElement("img");
        img.src = this.config.url;
        img.style.width = this.config.width;
        img.style.height = this.config.height;
        img.style.border = "1px solid #666";
        
        wrapper.appendChild(img);
        return wrapper;
    }
});
"""

with open(os.path.join(module_dir, "MMM-FaceFeed.js"), "w") as f:
    f.write(js_content)
    print("Created MMM-FaceFeed.js")

# 2. Update Config
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
                width: "320px"
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

config_path = os.path.join("MagicMirror", "config", "config.js")
try:
    with open(config_path, "w") as f:
        f.write(config_content)
    print(f"Successfully updated {config_path}")
except Exception as e:
    print(f"Error writing config: {e}")
