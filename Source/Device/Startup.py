import sys
import datetime
import threading
import time
import signal
import json
import Common
from modules import Battery
from modules import Button
from modules import Display
from pages import PageMain


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1}".format("Exiting", _signum))


def Button_Down(_button):
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

    bat = Battery.Battery()
    btn = Button.Button(_down=Button_Down)
    epp = Display.Display()
    Common.CurrentPage = PageMain.PageMain(epp)

    while Common.RUNNING:
        time.sleep(1)
        if Common.CurrentPage.RefreshTop():
            epp.imageChanged = True

    print("Exited")
