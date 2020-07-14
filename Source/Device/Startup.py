import threading
import time
import signal
import Common
import Battery
import Screen
import Button


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1} - {2}".format("Exit", _signum, _frame))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)
    Battery.Run()
    Screen.Run()
    Button.Run()

    while Common.RUNNING:
        time.sleep(0.1)

    time.sleep(0.5)
    print("Shutdown")

    #t1 = threading.Thread(target=run, args=("t1", ))
    #t2 = threading.Thread(target=run, args=("t2", ))
    #t1.start()
    #t2.start()