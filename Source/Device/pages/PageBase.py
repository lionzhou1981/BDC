import os
import json
import Common
from modules import Display
from PIL import Image, ImageDraw


class PageBase:
    def __init__(self, _display, _code):
        self.display = _display
        self.code = _code
        f = open(os.path.join(Common.PAGEDIR, "{0}.json".format(_code)), "r")
        self.page = json.loads(f.read())
        self.buttonSelected = -1
        self.buttons = []
        for item in self.page:
            if item[1] == "BUTTON":
                self.display.image = self.DrawButton(item, item[7])
                self.buttons.append(item)
            elif item[1] == "LABEL":
                self.display.image = self.DrawLabel(item)
            elif item[1] == "IMAGE":
                self.display.image = self.DrawImage(item)
        self.display.imageChanged = True

    def DrawButton(self, _item, _selected):
        draw = ImageDraw.Draw(self.display.image)
        draw.rectangle([(_item[2], _item[3]), _item[4], _item[5]], outline=255)
        font1 = self.GetFont(_item[7])
        size = font1.getsize(_item[6])
        draw.text([(_item[2], _item[3] + (_item[5] - size[1]) / 2), (_item[4], _item[5])], _item[6], align="center", font=font1)

    def DrawLabel(self, _item):
        draw = ImageDraw.Draw(self.display.image)
        height = font.getsize(_item[6])
        draw.text([(_item[2], _item[3] + (_item[5] - height) / 2), (_item[4], _item[5])], _item[6], align="center", font=self.GetFont(_item[7]))

    def DrawImage(self, _item):
        bmp = Image.open(os.path.join(Common.PICDIR, _item[6]))
        self.display.image.paste(bmp, (_item[2], _item[3]))

    def GetFont(self, _font):
        if _font == "NORMAL12":
            return Common.NORMAL12
        elif _font == "NORMAL20":
            return Common.NORMAL20

    def OnKeyUP(self, _key):
        return

    def OnKeyDOWN(self, _key):
        return

    def OnKeyLEFT(self, _key):
        return

    def OnKeyRIGHT(self, _key):
        return

    def OnKeyENTER(self, _key):
        return

    def OnKeyBACK(self, _key):
        return
