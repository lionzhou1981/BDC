import os
import time
import json
import Common
from pages import PageBase
from pages import PageMain
from pages import PageBBook
from pages import PageWord
from pages import PageBMission


class PageB(PageBase.PageBase):
    def __init__(self, _display):
        super(PageB, self).__init__(_display, "PageB", "TIME")

    def OnKeyENTER(self):
        btn = super().GetButton()
        print("Current: {0}".format(btn))
        if btn == "BUTTON_BOOK": super().GotoPage(PageBBook.PageBBook(self.display))
        elif btn == "BUTTON_RANDOM": super().GotoPage(PageWord.PageWord(self.display, Common.CurrentWords.random()))
        elif btn == "BUTTON_MISSION": super().GotoPage(PageBMission.PageBMission(self.display))

    def OnKeyBACK(self):
        super().GotoPage(PageMain.PageMain(self.display))

    def OnKeyLEFT(self):
        super().PrevButton()

    def OnKeyRIGHT(self):
        super().NextButton()
