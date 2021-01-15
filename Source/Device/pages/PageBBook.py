import os
import time
import json
import math
import Common
from pages import PageBase
from pages import PageMain
from pages import PageBBookUnit
from PIL import Image, ImageDraw


class PageBBook(PageBase.PageBase):
    def __init__(self, _display):
        self.pageImage = Image.new('1', (250, 960), 255)
        self.pageIndex = 0

        self.DrawLabel(['LABEL_KEY', 'LABEL', 4, -2, 121, 20, "英语（沪）", 'NORMAL20', 'LEFT'], self.pageImage)
        top = 0
        top = self.DrawLabel(['LABEL_SND', 'LABEL', 125, top, 111, 20, "英语（苏）", 'SYMBOL20', 'RIGHT'], self.pageImage)
        top = top + 2

    def OnKeyENTER(self):
        btn = super().GetButton()
        print("Current: {0}".format(btn))
        if btn == "BUTTON_C": super().GotoPage(PageC.PageC(self.display))
        elif btn == "BUTTON_B": super().GotoPage(PageB.PageB(self.display))

    def OnKeyBACK(self):
        super().GotoPage(PageMain.PageMain(self.display))

    def OnKeyUP(self):
        return

    def OnKeyDOWN(self):
        return

    def OnKeyLEFT(self):
        super().PrevButton()

    def OnKeyRIGHT(self):
        super().NextButton()
