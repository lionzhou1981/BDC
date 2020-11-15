import os
import time
import json
import Common
from pages import PageBase
from pages import PageBRandom
from pages import PageB


class PageWord1(PageBase.PageBase):
    def __init__(self, _display, _word):
        self.word = _word
        ui = '['
        ui = ui + '["LABEL_KEY","LABEL",4,28,112,24,"' + _word["code"] + '","NORMAL20","LEFT"],'
        ui = ui + '["LABEL_SND","LABEL",4,54,112,24,"' + _word["sound"] + '","LIGHT20","LEFT"]'
        ui = ui + ']'
        super(PageWord1, self).__init__(_display, "PageWord1", "TIME", json.loads(ui))

    def OnKeyENTER(self):
        Common.ReadText(self.word["code"], "en")

    def OnKeyBACK(self):
        super().GotoPage(PageBRandom.PageBRandom(self.display, false))

    def OnKeyUP(self):
        return

    def OnKeyDOWN(self):
        return

    def OnKeyLEFT(self):
        return

    def OnKeyRIGHT(self):
        super().GotoPage(PageWord1(self.display, Common.CurrentWords.random()))
