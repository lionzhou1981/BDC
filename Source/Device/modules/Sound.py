import os
import threading
import time
import Common


def Start():
    print("Sound Started")


def Stop():
    print("Sound Stopped")


def ReadText(_text, _lang, _speed=150, _amp=100):
    os.system("espeak -v {0} -s {1} -a {2} '{3}'".format(_lang, _speed, _amp, _text))
