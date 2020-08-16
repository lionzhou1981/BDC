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

FONT12 = ImageFont.truetype(os.path.join(Common.PICDIR, 'font.ttc'), 12)
FONT20 = ImageFont.truetype(os.path.join(Common.PICDIR, 'font.ttc'), 20)

print("Common init.")
