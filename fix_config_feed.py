import os

config_content = """/* Config with Nepal Settings - Working Online Khabar Feed */
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
			position: "top_left",
			config: {
				timezone: "Asia/Kathmandu",
				showDate: true,
				dateFormat: "dddd, LLL"
			}
		},
		{
			module: "calendar",
			header: "Nepal Holidays",
			position: "top_left",
			config: {
				calendars: [
					{
						symbol: "calendar-check",
						url: "https://www.officeholidays.com/ics/nepal"
					}
				],
				maximumEntries: 10,
				maximumNumberOfDays: 365
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
				lat: 27.7172,
				lon: 85.3240,
				roundTemp: true
			}
		},
		{
			module: "weather",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				weatherProvider: "openmeteo",
				type: "forecast",
				lat: 27.7172,
				lon: 85.3240,
				roundTemp: true
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "Online Khabar Nepal",
						url: "https://english.onlinekhabar.com/feed"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				updateInterval: 15000,
				reloadInterval: 300000
			}
		},
	]
};

if (typeof module !== "undefined") { module.exports = config; }
"""

config_path = os.path.join("MagicMirror", "config", "config.js")
with open(config_path, "w") as f:
    f.write(config_content)
    print("✓ Config updated with ONLY Online Khabar Nepal feed!")
    print("  URL: https://english.onlinekhabar.com/feed")
