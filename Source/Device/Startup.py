import threading
import time
import signal
import Common
import Battery
import Screen
import Button


def Exit(_signum, _frame):
    Common.RUNNING = False
    print("{0} - {1} - {2}".format("Exiting", _signum, _frame))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit)
    signal.signal(signal.SIGTERM, Exit)

    Battery.Run()
    Screen.Run()
    Audio.Run()
    Voice.Run()
    Button.Run()

    while Common.RUNNING:
        time.sleep(1)
        json = [["label_time", "label", 20, 20, 100, 40]]
        Screen.show(json)

    Battery.Stop()
    Screen.Stop()
    Audio.Stop()
    Voice.Stop()
    Button.Stop()

    time.sleep(0.5)
    print("Exited")

    #t1 = threading.Thread(target=run, args=("t1", ))
    #t2 = threading.Thread(target=run, args=("t2", ))
    #t1.start()
    #t2.start()