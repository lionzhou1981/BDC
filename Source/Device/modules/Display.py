import os
import time
import json
import Common
from PIL import Image, ImageDraw
from libs import epd_2in13


class Display:
    def __init__(self):
        self.epd = epd_2in13.EPD()
        self.epd.init(epd.FULL_UPDATE)
        self.image = Image.new('1', (epd.height, epd.width), 255)
        self.imageChanged = False
        self.ShowBase(image)
        _thread.start_new_thread(self.Run, ())
        print("Screen Started")

    def __del__(self):
        self.epd.init(epd.FULL_UPDATE)
        self.epd.Clear()
        self.epd.sleep()
        epd_2in13.epd_config.module_exit()
        print("Screen stopped")

    def Run(self):
        while Common.RUNNING:
            time.sleep(0.1)
            if self.imageChanged:
                self.ShowPart(self.image)

    def ShowBase(self, _image):
        self.epd.init(epd.FULL_UPDATE)
        self.epd.displayPartBaseImage(epd.getbuffer(image))
        self.epd.init(epd.PART_UPDATE)

    def ShowPart(self, _image):
        self.epd.displayPartBaseImage(epd.getbuffer(image))
