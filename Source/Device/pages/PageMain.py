import os
import time
import json
import Common
from pages import PageBase


class PageMain(PageBase.PageBase):
    def __init__(self, _display):
        super(PageMain, self).__init__(_display, "PageMain")

    def PrevButton():
        return

    def NextButton():
        return

    def OnKeyENTER(self, _key):
        return

    def OnKeyUP(self, _key):
        self.PreButton()

    def OnKeyDOWN(self, _key):
        self.NextButton()

    def OnKeyLEFT(self, _key):
        self.PrevButton()

    def OnKeyRIGHT(self, _key):
        self.NextButton()
