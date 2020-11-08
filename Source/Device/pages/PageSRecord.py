import os
import time
import json
import Common
from pages import PageBase
from pages import PageMain


class PageSRecord(PageBase.PageBase):
    def __init__(self, _display):
        super(PageSRecord, self).__init__(_display, "PageSRecord", "TIME")

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
