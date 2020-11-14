import os
import time
import _thread
import json
import Common


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
