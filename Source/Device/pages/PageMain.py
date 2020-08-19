import os
import time
import json
import Common
from pages import PageBase


class PageMain(PageBase.PageBase):
    def __init__(self, _display):
        super(PageMain, self).__init__(_display, "PageMain")

    def OnKeyENTER(self):
        return

    def OnKeyUP(self):
        super().PreButton()

    def OnKeyDOWN(self):
        super().NextButton()

    def OnKeyLEFT(self):
        super().PrevButton()

    def OnKeyRIGHT(self):
        super().NextButton()
