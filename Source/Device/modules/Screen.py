import os
import threading
import time
import json
import Common
from PIL import Image, ImageDraw, ImageFont
from libs import epd_2in13

epd = None
font12 = None
font20 = None
image = None


def Run():
    print("Screen starting")
    global epd
    global font12
    global font20
    font12 = ImageFont.load_default()
    font20 = ImageFont.load_default()
    #font12 = ImageFont.truetype(os.path.join(Common.PICDIR, 'Font.ttc'), 12)
    #font20 = ImageFont.truetype(os.path.join(Common.PICDIR, 'Font.ttc'), 20)
    epd = epd_2in13.EPD()
    print("Screen int and clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear()
    print("Screen ready")

    global image
    global draw
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    epd.displayPartBaseImage(epd.getbuffer(image))
    epd.init(epd.PART_UPDATE)
    print("Screen ready")


def Stop():
    print("Screen stopping")
    global epd
    epd.init()
    epd.Clear()
    epd.sleep()
    epd_2in13.epd_config.module_exit()
    print("Screen stopped")


def show(ui, value):
    global epd
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)

    for item in ui:
        if item[1] == "label":
            draw.rectangle((item[2], item[3], 240, 105), fill=255)
            draw.text((item[2], item[3]), value[item[0]], font=font20, fill=0)
            epd.displayPartial(epd.getbuffer(image))

    epd.displayPartBaseImage(epd.getbuffer(image))
