import json

BUTTON_PIN = [22, 12, 13, 16, 6, 27]
BUTTON_TXT = ["UP", "DOWN", "LEFT", "RIGHT", "ENTER", "BACK"]

SETTINGS = {}

with open("Config.json", "r", encoding='utf-8') as f:
    SETTINGS = json.loads(f.read())
