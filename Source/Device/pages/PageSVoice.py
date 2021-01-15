import os
from sys import setswitchinterval
import time
import json
import Common
import Config
from pages import PageBase
from pages import PageS


class PageSVoice(PageBase.PageBase):
    def __init__(self, _display):
        level = Config.SETTINGS["Voice"]
        l2_text = "男声"
        if level == "M": l2_text = "男声"
        elif level == "F": l2_text = "女声"

        l1 = ["LABEL-CURRENT", "LABEL", 10, 30, 90, 25, "人声选择:", "NORMAL16", "LEFT"]
        l2 = ["LABEL-READ", "LABEL", 100, 30, 40, 25, l2_text, "NORMAL16", "LEFT"]
        b1 = ["BUTTON-M", "BUTTON", 40, 65, 50, 50, "男声", "NORMAL20", 0, level == "M"]
        b2 = ["BUTTON-F", "BUTTON", 160, 65, 50, 50, "女声", "NORMAL20", 0, level == "F"]
        list = [l1, l2, b1, b2]
        super(PageSVoice, self).__init__(_display, "PageSVoice", "TIME", _page=list)

    def OnKeyENTER(self):
        super().GotoPage(PageS.PageS(self.display))

    def OnKeyBACK(self):
        super().GotoPage(PageS.PageS(self.display))

    def OnKeyLEFT(self):
        super().PrevButton()
        self.Switch()

    def OnKeyRIGHT(self):
        super().NextButton()
        self.Switch()

    def Switch(self):
        btn = super().GetButton()
        voice = "M"
        l2_text = "男声"
        if btn == "BUTTON-F":
            l2_text = "女声"
            voice = "F"

        Config.SETTINGS["Voice"] = voice
        Config.Save()
        l2 = ["LABEL-READ", "LABEL", 100, 30, 40, 25, l2_text, "NORMAL16", "LEFT"]
        self.DrawLabel(l2)
        self.display.imageChanged = True
