import os
import sys
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

NORMAL12 = ImageFont.truetype(os.path.join(PICDIR, 'normal.ttf'), 12)
NORMAL20 = ImageFont.truetype(os.path.join(PICDIR, 'normal.ttf'), 20)
NORMAL24 = ImageFont.truetype(os.path.join(PICDIR, 'normal.ttf'), 24)
LIGHT12 = ImageFont.truetype(os.path.join(PICDIR, 'light.ttf'), 12)
LIGHT20 = ImageFont.truetype(os.path.join(PICDIR, 'light.ttf'), 20)

CurrentPage = None

print("Common init.")


def ReadText(_text, _lang, _speed=150, _amp=100):
    os.system("espeak -v {0} -s {1} -a {2} '{3}'".format(_lang, _speed, _amp, _text))
