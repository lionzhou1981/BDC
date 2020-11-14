import sys
import datetime
import threading
import time
import signal
import json
import Common
from modules import Word


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1} - {2}".format("Exiting", _signum, _frame))


words = {}
if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    words = Word.Word()
    print(words.words)

    loop = 0
    while Common.RUNNING:
        time.sleep(1)
        loop = loop + 1
        print(words.random())

    time.sleep(0.5)
    print("Exited")
