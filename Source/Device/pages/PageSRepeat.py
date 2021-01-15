import Config
from pages import PageBase
from pages import PageS


class PageSRepeat(PageBase.PageBase):
    def __init__(self, _display):
        level = Config.SETTINGS["Repeat"]
        l2_text = "一"
        if level == 3: l2_text = "三"
        elif level == 5: l2_text = "五"
        else: level = 1

        l1 = ["LABEL-CURRENT", "LABEL", 10, 30, 90, 25, "重复次数:", "NORMAL16", "LEFT"]
        l2 = ["LABEL-READ", "LABEL", 100, 30, 40, 25, l2_text, "NORMAL16", "LEFT"]
        b1 = ["BUTTON-1", "BUTTON", 42, 65, 45, 45, "一", "NORMAL20", 0, level == "1"]
        b2 = ["BUTTON-3", "BUTTON", 101, 65, 45, 45, "三", "NORMAL20", 0, level == "3"]
        b3 = ["BUTTON-5", "BUTTON", 160, 65, 45, 45, "五", "NORMAL20", 0, level == "5"]
        list = [l1, l2, b1, b2, b3]
        super(PageSRepeat, self).__init__(_display, "PageSRepeat", "TIME", _page=list)

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
        level = 1
        l2_text = "一"
        if btn == "BUTTON-3":
            level = 3
            l2_text = "三"
        elif btn == "BUTTON-5":
            level = 5
            l2_text = "五"

        Config.SETTINGS["Repeat"] = level
        Config.Save()
        l2 = ["LABEL-READ", "LABEL", 100, 30, 40, 25, l2_text, "NORMAL16", "LEFT"]
        self.DrawLabel(l2)
        self.display.imageChanged = True