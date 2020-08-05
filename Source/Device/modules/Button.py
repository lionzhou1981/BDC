import _thread
import time
from RPi import GPIO
import Common

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # 关闭警告

channel0 = 19
channel1 = 26
channel2 = 12
channel3 = 16
channel4 = 20
channel5 = 21

clicked0 = 0
clicked1 = 0
clicked2 = 0
clicked3 = 0
clicked4 = 0
clicked5 = 0


def Run():
    GPIO.setup(channel0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(channel1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(channel2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(channel3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(channel4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(channel5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(channel0, GPIO.RISING, bouncetime=50)
    GPIO.add_event_detect(channel1, GPIO.RISING, bouncetime=50)
    GPIO.add_event_detect(channel2, GPIO.RISING, bouncetime=50)
    GPIO.add_event_detect(channel3, GPIO.RISING, bouncetime=50)
    GPIO.add_event_detect(channel4, GPIO.RISING, bouncetime=50)
    GPIO.add_event_detect(channel5, GPIO.RISING, bouncetime=50)
    _thread.start_new_thread(Loop, ())
    print("Button {0}".format(Common.RUNNING))


def Stop():
    print("Button {0}".format(Common.RUNNING))


def Loop():
    while Common.RUNNING:
        time.sleep(0.001)
        try:
            if GPIO.event_detected(channel0) and GPIO.input(
                    channel0) == GPIO.HIGH:
                print('Enter ')

            if GPIO.event_detected(channel1):
                print('Cancel')

            if GPIO.event_detected(channel2):
                print('UP')

            if GPIO.event_detected(channel3):
                print('DOWN')

            if GPIO.event_detected(channel4):
                print('LEFT')

            if GPIO.event_detected(channel5):
                print('RIGHT')

        except Exception as e:
            print(e)

    GPIO.cleanup()
