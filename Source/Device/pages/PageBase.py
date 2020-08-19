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
                self.DrawButton(item, item[9])
                self.buttons.append(item)
            elif item[1] == "LABEL":
                self.DrawLabel(item)
            elif item[1] == "IMAGE":
                self.DrawImage(item)
        self.display.imageChanged = True

    def DrawButton(self, _item, _selected):
        ax = _item[2]
        ay = _item[3]
        bx = _item[2] + item[4]
        by = _item[3] + item[5]
        text = _item[6]
        font = self.GetFont(_item[7])
        fontsize = font.getsize(_item[6])
        texty = ay + (by - fontsize[1]) / 2
        border = _item[8]
        draw = ImageDraw.Draw(self.display.image)
        if _selected:
            draw.rectangle([ax, ay, bx, by], fill=0, outline=0, width=border)
            draw.text((x, texty), _item[6], align="center", font=font, fill=255)
        else:
            draw.rectangle([ax, ay, bx, by], fill=255, outline=0, width=border)
            draw.text((x, texty), _item[6], align="center", font=font, fill=0)

    def DrawLabel(self, _item):
        draw = ImageDraw.Draw(self.display.image)
        height = font.getsize(_item[6])
        draw.text((_item[2], _item[3] + (_item[5] - height) / 2), _item[6], align="center", font=self.GetFont(_item[7]))

    def DrawImage(self, _item):
        bmp = Image.open(os.path.join(Common.PICDIR, _item[6]))
        self.display.image.paste(bmp, (_item[2], _item[3]))

    def GetFont(self, _font):
        if _font == "NORMAL12": return Common.NORMAL12
        elif _font == "NORMAL20": return Common.NORMAL20
        elif _font == "NORMAL24": return Common.NORMAL24
        elif _font == "LIGHT12": return Common.LIGHT12
        elif _font == "LIGHT20": return Common.LIGHT20

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
