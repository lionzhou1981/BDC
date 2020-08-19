import os
import json
import Common
from modules import Display
from PIL import Image, ImageDraw


class PageBase:
    def __init__(self, _display, _code):
        self.display = _display
        split = json.loads('["LINE_TOP","LINE",0,24,250,23,0,2]')
        self.DrawLine(split)
        self.DrawTop()
        self.code = _code
        f = open(os.path.join(Common.PAGEDIR, "{0}.json".format(_code)), "r")
        self.page = json.loads(f.read())
        self.buttonSelected = -1
        self.buttons = []
        buttonIndex = 0
        for item in self.page:
            if item[1] == "BUTTON":
                if self.buttonSelected > -1: self.DrawButton(item, False)
                else: self.DrawButton(item, item[9])
                self.buttons.append(item)
                if item[9] and self.buttonSelected == -1: self.buttonSelected = buttonIndex
                buttonIndex += 1
            elif item[1] == "LABEL":
                self.DrawLabel(item)
            elif item[1] == "IMAGE":
                self.DrawImage(item)
        self.display.imageChanged = True

    def DrawButton(self, _item, _selected):
        ax = _item[2]
        ay = _item[3]
        bx = _item[2] + _item[4]
        by = _item[3] + _item[5]
        text = _item[6]
        font = self.GetFont(_item[7])
        textsize = font.getsize(_item[6])
        tx = ax + (_item[4] - textsize[0]) / 2
        ty = ay + (_item[5] - textsize[1]) / 2
        border = _item[8]
        draw = ImageDraw.Draw(self.display.image)
        if _selected:
            draw.rectangle([ax, ay, bx, by], fill=0, outline=0, width=border)
            draw.text((tx, ty), _item[6], align="center", font=font, fill=255)
        else:
            draw.rectangle([ax, ay, bx, by], fill=255, outline=0, width=border)
            draw.text((tx, ty), _item[6], align="center", font=font, fill=0)

    def DrawLabel(self, _item):
        ax = _item[2]
        ay = _item[3]
        bx = _item[2] + _item[4]
        by = _item[3] + _item[5]
        draw = ImageDraw.Draw(self.display.image)
        height = font.getsize(_item[6])
        draw.text((_item[2], _item[3] + (_item[5] - height) / 2), _item[6], align="center", font=self.GetFont(_item[7]))

    def DrawImage(self, _item):
        bmp = Image.open(os.path.join(Common.PICDIR, _item[6]))
        self.display.image.paste(bmp, (_item[2], _item[3]))

    def DrawLine(self, _item):
        ax = _item[2]
        ay = _item[3]
        bx = _item[4]
        by = _item[5]
        color = _item[6]
        width = _item[7]
        draw = ImageDraw.Draw(self.display.image)
        draw.line([ax, ay, bx, by], fill=color, width=width)

    def DrawTop(self):
        return

    def GetFont(self, _font):
        if _font == "NORMAL12": return Common.NORMAL12
        elif _font == "NORMAL20": return Common.NORMAL20
        elif _font == "NORMAL24": return Common.NORMAL24
        elif _font == "LIGHT12": return Common.LIGHT12
        elif _font == "LIGHT20": return Common.LIGHT20

    def PrevButton(self):
        oldIndex = self.buttonSelected
        newIndex = oldIndex - 1
        if newIndex < 0: newIndex = len(self.buttons) - 1
        self.DrawButton(self.buttons[oldIndex], False)
        self.DrawButton(self.buttons[newIndex], True)
        self.buttonSelected = newIndex
        self.display.imageChanged = True

    def NextButton(self):
        oldIndex = self.buttonSelected
        newIndex = oldIndex + 1
        if newIndex >= len(self.buttons): newIndex = 0
        self.DrawButton(self.buttons[oldIndex], False)
        self.DrawButton(self.buttons[newIndex], True)
        self.buttonSelected = newIndex
        self.display.imageChanged = True

    def OnKeyUP(self):
        return

    def OnKeyDOWN(self):
        return

    def OnKeyLEFT(self):
        return

    def OnKeyRIGHT(self):
        return

    def OnKeyENTER(self):
        return

    def OnKeyBACK(self):
        return
