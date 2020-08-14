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


def Start():
    global epd
    global font12
    global font20
    global image

    font12 = ImageFont.truetype(os.path.join(Common.PICDIR, 'font.ttc'), 12)
    font20 = ImageFont.truetype(os.path.join(Common.PICDIR, 'font.ttc'), 20)
    epd = epd_2in13.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear()

    image = Image.new('1', (epd.height, epd.width), 255)
    ShowBase(image)
    print("Screen Started")


def Stop():
    global epd
    epd.init()
    epd.Clear()
    epd.sleep()
    epd_2in13.epd_config.module_exit()
    print("Screen stopped")


def ShowBase(_image):
    global epd
    epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(image))
    epd.init(epd.PART_UPDATE)


def ShowPart(_image):
    global epd
    epd.displayPartBaseImage(epd.getbuffer(image))


def ShowPage(_code):
    f = open(os.path.join(Common.PAGEDIR, "{0}.json".format(_code)), "r")
    page = json.loads(f.read())
    print(page)


#    for item in ui:
#        if item[1] == "label":
#            draw.rectangle((item[2], item[3], 240, 105), fill=255)
#            draw.text((item[2], item[3]), value[item[0]], font=font20, fill=0)
#            epd.displayPartial(epd.getbuffer(image))
