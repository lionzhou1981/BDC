import os
import threading
import time
import json
import Common
from PIL import Image, ImageDraw, ImageFont
from libs import epd2in13b_V2

epd = None
font12 = None
font20 = None


def Run():
    print("Screen starting")
    font12 = ImageFont.truetype(os.path.join(Common.PICDIR, 'Font.ttc'), 12)
    font20 = ImageFont.truetype(os.path.join(Common.PICDIR, 'Font.ttc'), 20)
    epd = epd2in13b_V2.EPD()
    print("Screen int and clear")
    epd.init()
    epd.Clear()

    time.sleep(1)
    print("Screen ready")


def Stop():
    print("Screen stopping")
    epd.init()
    epd.Clear()
    epd.sleep()
    print("Screen stopped")


def show(ui, value):
    ui_json = json.loads(ui)
    value_json = json.loads(value)

    HBlackimage = Image.new('1', (epd.height, epd.width), 255)
    HRYimage = Image.new('1', (epd.height, epd.width), 255)
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)

    for item in ui_json:
        if item[1] == "label":
            drawblack.text((item[2], item[3]), time.time(), font=font20, fill=0)

    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
