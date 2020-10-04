import os
import time
import _thread
import json
import Common
from PIL import Image, ImageDraw, ImageFont
from libs import epd_2in13

epd = epd_2in13.EPD()
epd.init(epd.FULL_UPDATE)
image = Image.new('1', (epd.height, epd.width), 255)
epd.init(epd.FULL_UPDATE)
epd.displayPartBaseImage(epd.getbuffer(_image))
epd.init(epd.PART_UPDATE)

num = 0
draw = ImageDraw.Draw(_image)
while (True):
    draw.rectangle((120, 80, 220, 105), fill=255)
    draw.text((120, 80), time.strftime('%H:%M:%S'), font=Common.NORMAL20, fill=0)
    epd.displayPartial(epd.getbuffer(_image))
    num = num + 1
    if (num == 10):
        break

epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)
epd.sleep()
