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
    print("{0} - {1} - {2}".format("Exiting", _signum, _frame))


def Button_Down(_button):
    if Common.CurrentPage == None: return
    if _button == "UP": Common.CurrentPage.OnKeyUP()
    elif _button == "DOWN": Common.CurrentPage.OnKeyUP()
    elif _button == "LEFT": Common.CurrentPage.OnKeyUP()
    elif _button == "RIGHT": Common.CurrentPage.OnKeyUP()
    elif _button == "BACK": Common.CurrentPage.OnKeyUP()
    elif _button == "ENTER": Common.CurrentPage.OnKeyUP()


def Button_Up(_button):
    print("Button {0} up.".format(_button))


def Show_UI(o, _code):
    if _code == "Main":
        Common.CurrentPage = PageMain.PageMain(o)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    if sys.argv[1] == "battery":
        o = Battery.Battery()
    elif sys.argv[1] == "button":
        o = Button.Button(_up=Button_Up, _down=Button_Down)
    elif sys.argv[1] == "ui":
        o = Display.Display()
        Show_UI(o, sys.argv[2])

    while Common.RUNNING:
        time.sleep(1)
        if sys.argv[1] == "battery":
            print("Battery: {0} - {1}".format(o.voltage, o.percent))

    time.sleep(0.5)
    print("Exited")
