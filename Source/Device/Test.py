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
from modules import Sound


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1} - {2}".format("Exiting", _signum, _frame))


def Start(_module):
    global Button_Clicked
    if sys.argv[1] == "battery":
        Battery.Start()
    elif sys.argv[1] == "display":
        Display.Start()
    elif sys.argv[1] == "button":
        Button.Start(_up=Button_Up, _down=Button_Down)
    elif sys.argv[1] == "sound":
        Sound.Start()


def Stop(_module):
    if sys.argv[1] == "battery":
        Battery.Stop()
    elif sys.argv[1] == "display":
        Display.Stop()
    elif sys.argv[1] == "button":
        Button.Stop()
    elif sys.argv[1] == "sound":
        Sound.Stop()


def Button_Down(_button):
    print("Button {0} down.".format(_button))


def Button_Up(_button):
    print("Button {0} up.".format(_button))


if __name__ == '__main__':
    Display.ShowPage("main")
    exit()
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    Start(sys.argv[1])

    while Common.RUNNING:
        time.sleep(1)

    Stop(sys.argv[1])

    time.sleep(0.5)
    print("Exited")
