import os

config_content = """/* Config with MMM-Remote-Control */
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
    print(f"Successfully wrote to {config_path}")
except Exception as e:
    print(f"Error writing config: {e}")
