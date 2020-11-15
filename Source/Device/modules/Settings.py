import os
import time
import _thread
import json
import Common


class Settings:
    def __init__(self):
        with open("../Settings.json", "r", encoding='utf-8') as f:
            self.data = json.loads(f.read())
        print("Settings stopped")

    def __del__(self):
        print("Settings stopped")

    def Get(self, key):
        return self.data[key]

    def Set(self, key, value):
        self.data[key] = value
        with open("../Settings.json", "w", encoding='utf-8') as f:
            f.write(json.dumps(self.data, indent=4))
