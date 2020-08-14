import _thread
import time
from RPi import GPIO
import Common

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # 关闭警告

PIN_NUM = [22, 12, 13, 16, 6, 27]
PIN_TXT = ["UP", "DOWN", "LEFT", "RIGHT", "ENTER", "BACK"]
PIN_HIT = [False, False, False, False, False, False]
EVENT_UP = None
EVENT_DOWN = None


def Start(_down=None, _up=None):
    global EVENT_UP
    global EVENT_DOWN
    EVENT_UP = _up
    EVENT_DOWN = _down
    for i in range(len(PIN_NUM)):
        PIN_HIT[i] = False
        GPIO.setup(PIN_NUM[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    _thread.start_new_thread(Run, ())
    print("Button Started")


def Stop():
    print("Button Stopped")


def Run():
    global EVENT_UP
    global EVENT_DOWN
    while Common.RUNNING:
        time.sleep(0.001)
        try:
            for i in range(len(PIN_NUM)):
                input = GPIO.input(PIN_NUM[i]) == 1
                if PIN_HIT[i] and input == False:
                    PIN_HIT[i] = False
                    if EVENT_UP != None:
                        EVENT_UP(PIN_TXT[i])
                elif PIN_HIT[i] == False and input:
                    PIN_HIT[i] = True
                    if EVENT_DOWN != None:
                        EVENT_DOWN(PIN_TXT[i])

        except Exception as e:
            print(e)

    GPIO.cleanup()
