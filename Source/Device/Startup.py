import datetime
import threading
import time
import signal
import json
import Common
import Battery
import Screen
import Button
import Audio
import Voice


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1} - {2}".format("Exiting", _signum, _frame))


def Button_Down(_button):
    print("Button {0} clicked.".format(_button))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    Battery.Start()
    Sound.Start()
    Button.Start(_down=Button_Down)

    while Common.RUNNING:
        time.sleep(1)
        ui = [["label_time", "label", 20, 20, 100, 40]]
        value = {'label_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Screen.show(ui, value)

    Button.Stop()
    Sound.Stop()
    Battery.Stop()

    time.sleep(0.5)
    print("Exited")
