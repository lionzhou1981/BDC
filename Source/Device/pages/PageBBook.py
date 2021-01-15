import os
import time
import json
import math
import Common
from pages import PageBase
from pages import PageMain
from PIL import Image


class PageBBook(PageBase.PageBase):
    def __init__(self, _display):
        self.pageImage = Image.new('1', (250, 960), 255)
        self.pageIndex = 0

        b1 = ["BUTTON-Z", "BUTTON", 20, 60, 44, 40, "静", "LIGHT16", 0, True]
        b2 = ["BUTTON-L", "BUTTON", 75, 60, 44, 40, "低", "LIGHT16", 0, False]

        list = [b1, b2]
        super(PageBBook, self).__init__(_display, "PageSVolume", "TIME", _page=list)

    def OnKeyENTER(self):
        btn = super().GetButton()
        print("Current: {0}".format(btn))
        #if btn == "BUTTON_C": super().GotoPage(PageC.PageC(self.display))
        #elif btn == "BUTTON_B": super().GotoPage(PageB.PageB(self.display))

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
