import os
import time
import json
import math
import Common
from pages import PageBase
from pages import PageB
from PIL import Image, ImageDraw


class PageWord(PageBase.PageBase):
    def __init__(self, _display, _word):
        self.word = _word
        self.pageImage = Image.new('1', (250, 960), 255)
        self.pageIndex = 0

        self.DrawLabel(['LABEL_KEY', 'LABEL', 4, -2, 121, 20, _word["code"], 'NORMAL20', 'LEFT'], self.pageImage)
        top = 0
        top = self.DrawLabel(['LABEL_SND', 'LABEL', 125, top, 111, 20, _word["sound"], 'SYMBOL20', 'RIGHT'], self.pageImage)
        top = top + 2

        for x in self.word["data"]:
            txt = "{0}: {1}".format(self.word["data"][x][0], self.word["data"][x][1])
            top = self.DrawLabel(['LABEL_TXT', 'LABEL', 4, top, 232, 16, txt, 'LIGHT16', 'LEFT'], self.pageImage)
            top = top + 2

        for x in self.word["data"]:
            for i in range(2, len(self.word["data"][x])):
                top = top + 2
                top = self.DrawLabel(['LABEL_TXT', 'LABEL', 4, top, 232, 16, self.word["data"][x][i], 'LIGHT16', 'LEFT'], self.pageImage)

        self.pageCount = math.ceil(top / 96)

        for x in range(0, self.pageCount):
            ax = 240
            ay = 96 - self.pageCount * 8 + x * 96 - 2
            for i in range(0, self.pageCount):
                by = ay + i * 8
                if i == x:
                    self.DrawBox(['PAGE', 'BOX', ax, by, 6, 6, True], self.pageImage)
                else:
                    self.DrawBox(['PAGE', 'BOX', ax, by, 6, 6, False], self.pageImage)

        super(PageWord, self).__init__(_display, "PageWord", "TIME", _image=self.pageImage)

    def OnKeyENTER(self):
        Common.ReadText(self.word["code"], "en")

    def OnKeyBACK(self):
        super().GotoPage(PageB.PageB(self.display))

    def OnKeyUP(self):
        self.pageIndex = self.pageIndex - 1
        if self.pageIndex <= 0: self.pageIndex = self.pageCount - 1
        self.DrawBlank([0, 28, 250, 120])
        img = Image.new('1', (250, 96), 255)
        img.paste(self.pageImage, (0, self.pageIndex * -96))
        self.display.image.paste(img, (0, 28))
        self.display.imageChanged = True

    def OnKeyDOWN(self):
        self.pageIndex = self.pageIndex + 1
        if self.pageIndex >= self.pageCount: self.pageIndex = 0
        self.DrawBlank([0, 28, 250, 120])
        img = Image.new('1', (250, 96), 255)
        img.paste(self.pageImage, (0, self.pageIndex * -96))
        self.display.image.paste(img, (0, 28))
        self.display.imageChanged = True

    def OnKeyLEFT(self):
        return

    def OnKeyRIGHT(self):
        super().GotoPage(PageWord(self.display, Common.CurrentWords.random()))
