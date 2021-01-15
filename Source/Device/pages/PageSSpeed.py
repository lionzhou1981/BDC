import Config
from pages import PageBase
from pages import PageS


class PageSSpeed(PageBase.PageBase):
    def __init__(self, _display):
        level = Config.SETTINGS["Speed"]
        l2_text = "中"
        if level == "L": l2_text = "慢"
        elif level == "H": l2_text = "快"
        else: level = "M"

        l1 = ["LABEL-CURRENT", "LABEL", 10, 30, 90, 25, "朗读速度:", "NORMAL16", "LEFT"]
        l2 = ["LABEL-READ", "LABEL", 100, 30, 40, 25, l2_text, "NORMAL16", "LEFT"]
        b1 = ["BUTTON-L", "BUTTON", 42, 65, 45, 45, "慢", "NORMAL20", 0, level == "L"]
        b2 = ["BUTTON-M", "BUTTON", 101, 65, 45, 45, "中", "NORMAL20", 0, level == "M"]
        b3 = ["BUTTON-H", "BUTTON", 160, 65, 45, 45, "快", "NORMAL20", 0, level == "H"]
        list = [l1, l2, b1, b2, b3]

        super(PageSSpeed, self).__init__(_display, "PageSSpeed", "TIME", _page=list)

    def OnKeyENTER(self):
        super().GotoPage(PageS.PageS(self.display))

    def OnKeyBACK(self):
        super().GotoPage(PageS.PageS(self.display))

    def OnKeyLEFT(self):
        super().PrevButton()
        self.Switch()

    def OnKeyRIGHT(self):
        super().NextButton()
        self.Switch()

    def Switch(self):
        btn = super().GetButton()
        speed = "M"
        l2_text = "中"
        if btn == "BUTTON-H":
            speed = "H"
            l2_text = "快"
        elif btn == "BUTTON-L":
            speed = "L"
            l2_text = "慢"

        Config.SETTINGS["Speed"] = speed
        Config.Save()
        l2 = ["LABEL-READ", "LABEL", 100, 30, 20, 25, l2_text, "NORMAL16", "LEFT"]
        self.DrawLabel(l2)
        self.display.imageChanged = True
