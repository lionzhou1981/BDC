import os
import time
import json
import Common
from pages import PageBase
from pages import PageMain
from pages import PageWord1


class PageBRandom(PageBase.PageBase):
    def __init__(self, _display, _next=False):
        if _next:
            super().GotoPage(PageWord1.PageWord1(_display, Common.CurrentWords.random()))
        else:
            super(PageBRandom, self).__init__(_display, "PageBRandom", "TIME")

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

    def OnKeyRIGHT(self):
        super().NextButton()