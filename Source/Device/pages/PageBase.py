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

    def DrawButton(self, _item, _selected):
        draw = ImageDraw.Draw(self.display.image)
        draw.rectangle([(_item[1], _item[2]), (_item[3], _item[4])], outline=1)
        height = font.getsize(_item[5])
        draw.text([(_item[1], _item[2] + (_item[4] - height) / 2), (_item[3], _item[4])], _item[5], align="center", font=self.GetFont(_item[6]))

    def DrawLabel(self, _item):
        draw = ImageDraw.Draw(self.display.image)
        height = font.getsize(_item[6])
        draw.text([(_item[1], _item[2] + (_item[4] - height) / 2), (_item[3], _item[4])], _item[5], align="center", font=self.GetFont(_item[6]))

    def DrawImage(self, _item):
        bmp = Image.open(os.path.join(Common.PICDIR, _item[5]))
        self.display.image.paste(bmp, (_item[1], _item[2]))

    def GetFont(self, _font):
        if _font == "NORMAL12":
            return Common.FONT12
        elif _font == "NORMAL20":
            return Common.FONT20

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
