import _thread
import time
from RPi import GPIO
import Common


class Button:
    def __init__(self, _down=None, _up=None):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # 关闭警告
        self.PIN_NUM = [22, 12, 13, 16, 6, 27]
        self.PIN_TXT = ["UP", "DOWN", "LEFT", "RIGHT", "ENTER", "BACK"]
        self.PIN_HIT = [False, False, False, False, False, False]
        self.EVENT_UP = _up
        self.EVENT_DOWN = _down
        for i in range(len(self.PIN_NUM)):
            self.PIN_HIT[i] = False
            GPIO.setup(self.PIN_NUM[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        _thread.start_new_thread(self.Run, ())
        print("Button Started")

    def __del__(self):
        print("Button Stopped")

    def Run(self):
        while Common.RUNNING:
            time.sleep(0.001)
            try:
                for i in range(len(self.PIN_NUM)):
                    input = GPIO.input(self.PIN_NUM[i]) == 1
                    if self.PIN_HIT[i] and input == False:
                        self.PIN_HIT[i] = False
                        if self.EVENT_UP != None:
                            self.EVENT_UP(self.PIN_TXT[i])
                    elif self.PIN_HIT[i] == False and input:
                        self.PIN_HIT[i] = True
                        if self.EVENT_DOWN != None:
                            self.EVENT_DOWN(self.PIN_TXT[i])

            except Exception as e:
                print(e)

        GPIO.cleanup()
