import os
from sys import setswitchinterval
import time
import json
import Common
import Config
from pages import PageBase
from pages import PageMain
from pages import PageB
from PIL import Image


class PageSRecord(PageBase.PageBase):
    def __init__(self, _display):
        level = Config.SETTINGS["Record"]
        l2_text = "高"
        if level == "Z": l2_text = "静"
        elif level == "L": l2_text = "低"
        elif level == "M": l2_text = "中"
        else: level = "H"

        l1 = ["LABEL-CURRENT", "LABEL", 10, 30, 90, 25, "当前状态:", "NORMAL16", "LEFT"]
        l2 = ["LABEL-READ", "LABEL", 100, 30, 20, 25, l2_text, "NORMAL16", "LEFT"]
        b1 = ["BUTTON-Z", "BUTTON", 20, 60, 44, 40, "静", "LIGHT16", 0, level == "Z"]
        b2 = ["BUTTON-L", "BUTTON", 75, 60, 44, 40, "低", "LIGHT16", 0, level == "L"]
        b3 = ["BUTTON-M", "BUTTON", 131, 60, 44, 40, "中", "LIGHT16", 0, level == "M"]
        b4 = ["BUTTON-H", "BUTTON", 186, 60, 44, 40, "高", "LIGHT16", 0, level == "H"]
        list = [l1, l2, b1, b2, b3, b4]
        super(PageSRecord, self).__init__(_display, "PageSRecord", "TIME", _page=list)

    def OnKeyENTER(self):
        return

    def OnKeyBACK(self):
        super().GotoPage(PageB.PageB(self.display))

    def OnKeyUP(self):
        return

    def OnKeyDOWN(self):
        return

    def OnKeyLEFT(self):
        super().PrevButton()
        self.Switch()

    def OnKeyRIGHT(self):
        super().NextButton()
        self.Switch()

    def Switch(self):
        btn = super().GetButton()
        level = "H"
        l2_text = "高"
        if btn == "BUTTON-Z":
            level = "Z"
            l2_text = "静"
        elif btn == "BUTTON-L":
            level = "L"
            l2_text = "低"
        elif btn == "BUTTON-M":
            level = "M"
            l2_text = "中"
        Config.SETTINGS["Record"] = level
        Config.SetRecord()
        Config.Save()
        l2 = ["LABEL-READ", "LABEL", 100, 30, 20, 25, l2_text, "NORMAL16", "LEFT"]
        self.DrawLabel(l2)
        self.display.imageChanged = True
