import os
from sys import setswitchinterval
import time
import json
import Common
import Config
from pages import PageBase
from pages import PageS
from PIL import Image


class PageSVolume(PageBase.PageBase):
    def __init__(self, _display):
        list = []
        l1 = ["LABEL-CURRENT", "LABEL", 10, 30, 90, 25, "当前状态:", "NORMAL16", "LEFT"]

        level = Config.SETTINGS["Volume"]
        l2_text = "高"
        if level == "Z": l2_text = "静"
        elif level == "L": l2_text = "低"
        elif level == "M": l2_text = "中"
        else: level = "H"

        l2 = ["LABEL-READ", "LABEL", 100, 30, 20, 25, l2_text, "NORMAL16", "LEFT"]
        b1 = ["BUTTON-Z", "BUTTON", 20, 60, 44, 40, "静", "LIGHT16", 0, level == "Z"]
        b2 = ["BUTTON-L", "BUTTON", 75, 60, 44, 40, "低", "LIGHT16", 0, level == "L"]
        b3 = ["BUTTON-M", "BUTTON", 131, 60, 44, 40, "中", "LIGHT16", 0, level == "M"]
        b4 = ["BUTTON-H", "BUTTON", 186, 60, 44, 40, "高", "LIGHT16", 0, level == "H"]
        list.append(l1)
        list.append(l2)
        list.append(b1)
        list.append(b2)
        list.append(b3)
        list.append(b4)

        super(PageSVolume, self).__init__(_display, "PageSVolume", "TIME", _page=list)

    def OnKeyENTER(self):
        return

    def OnKeyBACK(self):
        super().GotoPage(PageS.PageS(self.display))

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
        Config.SETTINGS["Volume"] = level
        Config.SetVolume()
        Config.Save()
        l2 = ["LABEL-READ", "LABEL", 100, 30, 20, 25, l2_text, "NORMAL16", "LEFT"]
        self.DrawLabel(l2)
        self.display.imageChanged = True