from pages import PageBase
from pages import PageMain
from pages import PageSVolume
from pages import PageSRecord
from pages import PageSVoice
from pages import PageSSpeed
from pages import PageSRepeat


class PageS(PageBase.PageBase):
    def __init__(self, _display):
        super(PageS, self).__init__(_display, "PageS", "TIME")

    def OnKeyENTER(self):
        btn = self.GetButton()
        if btn == "BUTTON-VOLUME":
            super().GotoPage(PageSVolume.PageSVolume(self.display))
        elif btn == "BUTTON-RECORD":
            super().GotoPage(PageSRecord.PageSRecord(self.display))
        elif btn == "BUTTON-VOICE":
            super().GotoPage(PageSVoice.PageSVoice(self.display))
        elif btn == "BUTTON-SPEED":
            super().GotoPage(PageSSpeed.PageSSpeed(self.display))
        elif btn == "BUTTON-REPEAT":
            super().GotoPage(PageSRepeat.PageSRepeat(self.display))

    def OnKeyBACK(self):
        super().GotoPage(PageMain.PageMain(self.display))

    def OnKeyUP(self):
        btn = self.GetButton()
        if btn == "BUTTON-VOLUME":
            self.PrevButton(3)
        elif btn == "BUTTON-RECORD":
            self.PrevButton(4)
        elif btn == "BUTTON-NETWORK":
            self.PrevButton(5)
        elif btn == "BUTTON-VOICE":
            self.PrevButton(0)
        elif btn == "BUTTON-SPEED":
            self.PrevButton(1)
        elif btn == "BUTTON-REPEAT":
            self.PrevButton(2)

    def OnKeyDOWN(self):
        btn = self.GetButton()
        if btn == "BUTTON-VOLUME":
            self.NextButton(3)
        elif btn == "BUTTON-RECORD":
            self.NextButton(4)
        elif btn == "BUTTON-NETWORK":
            self.PrevButton(5)
        elif btn == "BUTTON-VOICE":
            self.NextButton(0)
        elif btn == "BUTTON-SPEED":
            self.NextButton(1)
        elif btn == "BUTTON-REPEAT":
            self.PrevButton(2)

    def OnKeyLEFT(self):
        btn = self.GetButton()
        if btn == "BUTTON-VOLUME":
            self.PrevButton(2)
        elif btn == "BUTTON-RECORD":
            self.PrevButton(0)
        elif btn == "BUTTON-NETWORK":
            self.PrevButton(1)
        elif btn == "BUTTON-VOICE":
            self.PrevButton(5)
        elif btn == "BUTTON-SPEED":
            self.PrevButton(3)
        elif btn == "BUTTON-REPEAT":
            self.PrevButton(4)

    def OnKeyRIGHT(self):
        btn = self.GetButton()
        if btn == "BUTTON-VOLUME":
            self.NextButton(1)
        elif btn == "BUTTON-RECORD":
            self.NextButton(2)
        elif btn == "BUTTON-NETWORK":
            self.PrevButton(0)
        elif btn == "BUTTON-VOICE":
            self.NextButton(4)
        elif btn == "BUTTON-SPEED":
            self.NextButton(5)
        elif btn == "BUTTON-REPEAT":
            self.NextButton(3)
