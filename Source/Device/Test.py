import sys
import datetime
import threading
import time
import signal
import json
import Common
from modules import Battery


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1} - {2}".format("Exiting", _signum, _frame))


def Start(_module):
    if sys.argv[1] == "battery":
        Battery.Start()


def Stop(_module):
    if sys.argv[1] == "battery":
        Battery.Stop()


def Test(_module):
    if sys.argv[1] == "battery":
        Battery.Test()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    Start(sys.argv[1])

    while Common.RUNNING:
        time.sleep(1)
        Test(sys.argv[1])

    Stop(sys.argv[1])

    time.sleep(0.5)
    print("Exited")
