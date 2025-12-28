import os

module_dir = os.path.join("MagicMirror", "modules", "MMM-FaceFeed")

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
    font-weight: normal;
    font-family: Arial, sans-serif;
}
"""

with open(os.path.join(module_dir, "MMM-FaceFeed.css"), "w") as f:
    f.write(css_content)
    print("Updated CSS - changed to normal font weight")
