import subprocess
import json

BUTTON_PIN = [22, 12, 13, 16, 6, 27]
BUTTON_TXT = ["UP", "DOWN", "LEFT", "RIGHT", "ENTER", "BACK"]

with open("Config.json", "r", encoding='utf8') as fp:
    SETTINGS = json.loads(fp.read())
print(SETTINGS)


def LoadAll():
    SetVolume()
    SetRecord()


def Save():
    with open("Config.json", "w", encoding='utf8') as fp:
        fp.write(json.dumps(SETTINGS, indent=4, ensure_ascii=False))


def SetVolume():
    if SETTINGS["Volume"] == "Z":
        subprocess.call(["amixer", "set", "PCM", "0%"])
    elif SETTINGS["Volume"] == "L":
        subprocess.call(["amixer", "set", "PCM", "30%"])
    elif SETTINGS["Volume"] == "M":
        subprocess.call(["amixer", "set", "PCM", "60%"])
    else:
        SETTINGS["Volume"] = "H"
        subprocess.call(["amixer", "set", "PCM", "95%"])


def SetRecord():
    if SETTINGS["Record"] == "Z":
        subprocess.call(["amixer", "set", "Boost", "0%"])
    elif SETTINGS["Record"] == "L":
        subprocess.call(["amixer", "set", "Boost", "30%"])
    elif SETTINGS["Record"] == "M":
        subprocess.call(["amixer", "set", "Boost", "62%"])
    else:
        SETTINGS["Record"] = "H"
        subprocess.call(["amixer", "set", "Boost", "95%"])
