import os
import time
import json
import Common
from modules import Display
from PIL import Image, ImageDraw


class PageBase:
    def __init__(self, _display, _code, _title, _page=None):
        self.display = _display
        self.code = _code
        self.title = _title
        self.title_text = None
        self.title_battery = None
        self.DrawBlank()
        self.DrawLine(json.loads('["LINE_TOP","LINE",0,24,250,23,0,2]'))
        if _page == None:
            self.page = json.loads(open(os.path.join(Common.PAGEDIR, "{0}.json".format(_code)), "r").read())
        else:
            self.page = _page
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
            elif item[1] == "LINE":
                self.DrawLine(item)
        print("Page: {0} - Button: {1}".format(_code, len(self.buttons)))
        Common.CurrentPage = self
        self.RefreshTop()
        self.display.imageChanged = True

    def RefreshTop(self):
        update = False
        if self.title == "TIME":
            now = time.strftime("%Y-%m-%d %H:%M ")
            if self.title_text != now:
                self.DrawTitle(now)
                self.title_text = now
                update = True
        elif self.title_text == None:
            self.DrawTitle(self.title)
            self.title_text = self.title
            update = True
        if Common.CurrentBattery != None:
            if Common.CurrentBattery == 999: level = "c"
            elif Common.CurrentBattery > 70: level = "h"
            elif Common.CurrentBattery > 30: level = "m"
            else: level = "l"
            if self.title_battery != level:
                self.DrawBattery(level)
                self.title_battery = level
                update = True
        return update

    def DrawBlank(self):
        draw = ImageDraw.Draw(self.display.image)
        draw.rectangle([0, 25, 250, 120], fill=255, outline=0, width=0)

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
            draw.text((tx, ty), _item[6], font=font, fill=255)
        else:
            draw.rectangle([ax, ay, bx, by], fill=255, outline=0, width=border)
            draw.text((tx, ty), _item[6], font=font, fill=0)

    def DrawLabel(self, _item):
        ax = _item[2]
        ay = _item[3]
        bx = _item[2] + _item[4]
        by = _item[3] + _item[5]
        text = _item[6]
        font = self.GetFont(_item[7])
        align = _item[8]
        textsize = font.getsize(_item[6])
        draw = ImageDraw.Draw(self.display.image)
        draw.rectangle([ax, ay, bx, by], fill=255)
        if align == "LEFT":
            draw.text((ax, ay), _item[6], font=font, fill=0)
        elif align == "CENTER":
            tx = ax + (_item[4] - textsize[0]) / 2
            draw.text((tx, ay), _item[6], font=font, fill=0)
        elif align == "RIGHT":
            tx = bx - textsize[0]
            draw.text((tx, ay), _item[6], font=font, fill=0)

    def DrawImage(self, _item):
        ax = _item[2]
        ay = _item[3]
        bx = _item[2] + _item[4]
        by = _item[3] + _item[5]
        draw = ImageDraw.Draw(self.display.image)
        draw.rectangle([ax, ay, bx, by], fill=255)
        bmp = Image.open(os.path.join(Common.PICDIR, _item[6]))
        self.display.image.paste(bmp, (ax, ay))

    def DrawLine(self, _item):
        ax = _item[2]
        ay = _item[3]
        bx = _item[4]
        by = _item[5]
        color = _item[6]
        width = _item[7]
        draw = ImageDraw.Draw(self.display.image)
        draw.line([ax, ay, bx, by], fill=color, width=width)

    def DrawTitle(self, _title):
        label_time = json.loads('["LABEL_TIME","LABEL",3,3,150,14,"{0}","NORMAL14","LEFT"]'.format(_title))
        self.DrawLabel(label_time)

    def DrawBattery(self, _level):
        image_battary = json.loads('["IMAGE_BATTERY","IMAGE",230,4,16,16,"bat_{0}.jpg"]'.format(_level))
        self.DrawImage(image_battary)

    def GetFont(self, _font):
        if _font == "NORMAL14": return Common.NORMAL14
        elif _font == "NORMAL20": return Common.NORMAL20
        elif _font == "NORMAL24": return Common.NORMAL24
        elif _font == "LIGHT12": return Common.LIGHT12
        elif _font == "LIGHT20": return Common.LIGHT20
        elif _font == "SYMBOL20": return Common.SYMBOL20

    def PrevButton(self):
        oldIndex = self.buttonSelected
        newIndex = oldIndex - 1
        if newIndex < 0: newIndex = len(self.buttons) - 1
        self.DrawButton(self.buttons[oldIndex], False)
        self.DrawButton(self.buttons[newIndex], True)
        self.buttonSelected = newIndex
        print("Page:{0} - Prev: {1} -> {2}".format(self.code, oldIndex, newIndex))
        self.display.imageChanged = True

    def NextButton(self):
        oldIndex = self.buttonSelected
        newIndex = oldIndex + 1
        if newIndex >= len(self.buttons): newIndex = 0
        self.DrawButton(self.buttons[oldIndex], False)
        self.DrawButton(self.buttons[newIndex], True)
        self.buttonSelected = newIndex
        print("Page:{0} - Next: {1} -> {2}".format(self.code, oldIndex, newIndex))
        self.display.imageChanged = True

    def GetButton(self):
        return self.buttons[self.buttonSelected][0]

    def GotoPage(self, _page):
        Common.CurrentPage = _page

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
