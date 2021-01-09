import sys
import datetime
import threading
import time
import signal
import json
import Common
import Config
from modules import Battery
from modules import Button
from modules import Display
from modules import Word
from pages import PageMain


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1}".format("Exiting", _signum))


def Button_Down(_button):
    print("Button: {0}".format(_button))
    if Common.CurrentPage == None: return
    if _button == "UP": Common.CurrentPage.OnKeyUP()
    elif _button == "DOWN": Common.CurrentPage.OnKeyDOWN()
    elif _button == "LEFT": Common.CurrentPage.OnKeyLEFT()
    elif _button == "RIGHT": Common.CurrentPage.OnKeyRIGHT()
    elif _button == "BACK": Common.CurrentPage.OnKeyBACK()
    elif _button == "ENTER": Common.CurrentPage.OnKeyENTER()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    Config.LoadAll()

    bat = Battery.Battery()
    btn = Button.Button(_down=Button_Down)
    scr = Display.Display()
    Common.CurrentWords = Word.Word()
    top = PageMain.PageMain(scr)

    while Common.RUNNING:
        time.sleep(1)
        if Common.CurrentPage.RefreshTop():
            scr.imageChanged = True

    print("Exited")
