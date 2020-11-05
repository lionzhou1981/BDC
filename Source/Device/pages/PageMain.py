import os
import time
import json
import Common
from pages import PageBase
from pages import PageC
from pages import PageB
from pages import PageS


class PageMain(PageBase.PageBase):
    def __init__(self, _display):
        super(PageMain, self).__init__(_display, "PageMain", "TIME")

    def OnKeyENTER(self):
        btn = super().GetButton()
        print("Current: {0}".format(btn))
        if btn == "BUTTON_C": super().GotoPage(PageC.PageC(self.display))
        elif btn == "BUTTON_B": super().GotoPage(PageB.PageB(self.display))
        elif btn == "BUTTON_T": super().GotoPage(PageT.PageT(self.display))
        elif btn == "BUTTON_S": super().GotoPage(PageS.PageS(self.display))

    def OnKeyUP(self):
        return

    def OnKeyDOWN(self):
        return

    def OnKeyLEFT(self):
        super().PrevButton()

    def OnKeyRIGHT(self):
        super().NextButton()
