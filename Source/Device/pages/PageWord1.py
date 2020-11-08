import os
import time
import json
import Common
from pages import PageBase
from pages import PageMain


class Pageword1(PageBase.PageBase):
    def __init__(self, _display):
        super(Pageword1, self).__init__(_display, "Pageword1", "TIME")

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
