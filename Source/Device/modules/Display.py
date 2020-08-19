import os
import time
import _thread
import json
import Common
from PIL import Image, ImageDraw
from libs import epd_2in13


class Display:
    def __init__(self):
        self.epd = epd_2in13.EPD()
        self.epd.init(self.epd.FULL_UPDATE)
        self.image = Image.new('1', (self.epd.height, self.epd.width), 255)
        self.imageChanged = False
        self.ShowBase(self.image)
        _thread.start_new_thread(self.Run, ())
        print("Display Started")

    def __del__(self):
        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.Clear(0xFF)
        self.epd.sleep()
        print("Display stopped")

    def Run(self):
        while Common.RUNNING:
            time.sleep(0.1)
            if self.imageChanged:
                self.imageChanged = False
                print("changed")
                self.ShowPart(self.image)

    def ShowBase(self, _image):
        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.displayPartBaseImage(self.epd.getbuffer(_image))
        self.epd.init(self.epd.PART_UPDATE)

    def ShowPart(self, _image):
        self.epd.displayPartial(self.epd.getbuffer(_image))
