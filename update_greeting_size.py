import os

module_dir = os.path.join("MagicMirror", "modules", "MMM-FaceFeed")

css_content = """.greeting-container {
    padding: 15px 25px;
    background-color: transparent;
    border: 2px solid white;
    text-align: center;
    border-radius: 8px;
    max-width: 350px;
}

.greeting-text {
    font-size: 28px;
    color: white;
    font-weight: 300;
    font-family: Arial, sans-serif;
    line-height: 1.2;
}
"""

with open(os.path.join(module_dir, "MMM-FaceFeed.css"), "w") as f:
    f.write(css_content)
    print("✓ Updated CSS - smaller (28px), thinner (300 weight)")
    print("✓ Reduced padding and added max-width to prevent overlap")
