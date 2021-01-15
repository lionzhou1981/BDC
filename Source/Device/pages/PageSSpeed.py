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

class PageSSpeed(PageBase.PageBase):
    def __init__(self, _display):
        list = []
        l1 = ["LABEL-CURRENT", "LABEL", 10, 30, 90, 25, "当前状态:", "NORMAL16", "LEFT"]

        level = Config.SETTINGS["Speed"]
        l2_text = "中"
        if level == "1": l2_text = "慢"
        elif level == "3": l2_text = "中"
        elif level == "5": l2_text = "快"

        l2 = ["LABEL-READ", "LABEL", 100, 30, 40, 25, l2_text, "NORMAL16", "LEFT"]
        b1 = ["BUTTON-ONE","BUTTON",42,65,45,45,"慢","NORMAL20",0,level == "1"]
        b2 = ["BUTTON-THREE","BUTTON",101,65,45,45,"中","NORMAL20",0,level == "3"]
        b3 = ["BUTTON-FIVE","BUTTON",160,65,45,45,"快","NORMAL20",0,level == "5"]
        
        list.append(l1)
        list.append(l2)
        list.append(b1)
        list.append(b2)
        list.append(b3)
        super(PageSSpeed, self).__init__(_display, "PageSSpeed", "TIME",_page=list)

    def OnKeyENTER(self):
        return

    def OnKeyBACK(self):
        super().GotoPage(PageMain.PageMain(self.display))

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
        level = "1"
        l2_text = "慢"
        if btn == "BUTTON-Z":
            level = "3"
            l2_text = "中"
        elif btn == "BUTTON-L":
            level = "5"
            l2_text = "快"
       
        Config.SETTINGS["Repeat"] = level
        Config.SetRepeat()
        Config.Save()
        l2 = ["LABEL-READ", "LABEL", 100, 30, 20, 25, l2_text, "NORMAL16", "LEFT"]
        self.DrawLabel(l2)
        self.display.imageChanged = True
