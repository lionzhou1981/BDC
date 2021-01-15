import os
import sys
import Config
from PIL import ImageFont

RUNNING = True

PICDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pics')
LIBDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'libs')
MODDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modules')
PAGEDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pages')

if os.path.exists(LIBDIR):
    sys.path.append(LIBDIR)

if os.path.exists(MODDIR):
    sys.path.append(MODDIR)

LIGHT14 = ImageFont.truetype(os.path.join(PICDIR, 'light.ttf'), 14)
LIGHT16 = ImageFont.truetype(os.path.join(PICDIR, 'light.ttf'), 16)

NORMAL16 = ImageFont.truetype(os.path.join(PICDIR, 'normal.ttf'), 16)
NORMAL20 = ImageFont.truetype(os.path.join(PICDIR, 'normal.ttf'), 20)
NORMAL24 = ImageFont.truetype(os.path.join(PICDIR, 'normal.ttf'), 24)

SYMBOL16 = ImageFont.truetype(os.path.join(PICDIR, 'symbol.ttf'), 16)

CurrentPage = None
CurrentBattery = None
CurrentWords = None

print("Common init.")


def ReadText(_text, _lang):
    if Config.SETTINGS["Voice"] == "F":
        _lang = _lang + "+f2"

    if Config.SETTINGS["Speed"] == "H":
        _speed = 180
    elif Config.SETTINGS["Speed"] == "M":
        _speed = 140
    else:
        _speed = 100

    os.system("espeak -v {0} -s {1} '{2}'".format(_lang, _speed, _text))
    for i in range(1, Config.SETTINGS["Repeat"]):
        os.system("espeak -v {0} -s {1} '{2}'".format(_lang, _speed, _text))
