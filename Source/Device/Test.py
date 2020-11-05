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
from pages import PageC
from pages import PageB
from pages import PageS


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1} - {2}".format("Exiting", _signum, _frame))


def Button_Down(_button):
    print("Button: {0}".format(_button))
    if Common.CurrentPage == None: return
    if _button == "UP": Common.CurrentPage.OnKeyUP()
    elif _button == "DOWN": Common.CurrentPage.OnKeyDOWN()
    elif _button == "LEFT": Common.CurrentPage.OnKeyLEFT()
    elif _button == "RIGHT": Common.CurrentPage.OnKeyRIGHT()
    elif _button == "BACK": Common.CurrentPage.OnKeyBACK()
    elif _button == "ENTER": Common.CurrentPage.OnKeyENTER()


def Show_UI(o, _code):
    if _code == "Main": Common.CurrentPage = PageMain.PageMain(o)
    if _code == "C": Common.CurrentPage = PageC.PageC(o)
    if _code == "B": Common.CurrentPage = PageB.PageB(o)
    if _code == "S": Common.CurrentPage = PageS.PageS(o)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    btn = Button.Button(_down=Button_Down)
    bat = Battery.Battery()
    scr = Display.Display()

    loop = 0
    while Common.RUNNING:
        time.sleep(1)
        if sys.argv[1] == "battery":
            print("Battery: {0} - {1}".format(bat.voltage, bat.percent))
        elif sys.argv[1] == "ui" and loop == 0:
            Show_UI(scr, sys.argv[2])
        loop = loop + 1

    time.sleep(0.5)
    print("Exited")
