import os
import json
import Common
from modules import Display
from PIL import Image, ImageDraw


class PageBase:
    def __init__(self, _code):
        global epd
        global image
        self.code = _code
        f = open(os.path.join(Common.PAGEDIR, "{0}.json".format(_code)), "r")
        self.page = json.loads(f.read())
        self.buttonSelected = -1
        self.buttons = []
        for item in self.page:
            if item[1] == "BUTTON":
                image = self.DrawButton(image, item, item[7])
                self.buttons.append(item)
            elif item[1] == "LABEL":
                image = self.DrawLabel(image, item)
            elif item[1] == "IMAGE":
                image = self.DrawImage(image, item)

    def DrawButton(self, _image, _item, _selected):
        draw = ImageDraw.Draw(_image)
        draw.rectangle([(_item[1], _item[2]), (_item[3], _item[4])], outline=1)
        height = font.getsize(_item[5])
        draw.text([(_item[1], _item[2] + (_item[4] - height) / 2), (_item[3], _item[4])], _item[5], align="center", font=self.GetFont(_item[6]))
        return _image

    def DrawLabel(self, _image, _item):
        draw = ImageDraw.Draw(_image)
        height = font.getsize(_item[6])
        draw.text([(_item[1], _item[2] + (_item[4] - height) / 2), (_item[3], _item[4])], _item[5], align="center", font=self.GetFont(_item[6]))
        return _image

    def DrawImage(self, _image, _item):
        bmp = Image.open(os.path.join(Common.PICDIR, _item[5]))
        _image.paste(bmp, (_item[1], _item[2]))
        return _image

    def GetBaseImage(self):
        return

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
