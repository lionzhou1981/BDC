import _thread
import time
import os
import smbus
import Common
import RPi.GPIO as GPIO

value = -1

HW = smbus.SMBus(1)
VCELL_REGISTER = 0x02
SOC_REGISTER = 0x04
MODE_REGISTER = 0x06
VERSION_REGISTER = 0x08
CONFIG_REGISTER = 0x0C
COMMAND_REGISTER = 0xFE


def Start():
    reset()
    run()
    _thread.start_new_thread(Loop, ())
    print("Battery {0}".format(Common.RUNNING))


def Stop():
    print("Battery {0}".format(Common.RUNNING))


def Test():
    global value
    print("Battery {0}".format(value))


def Loop():
    cd = 10
    while Common.RUNNING:
        time.sleep(0.1)
        cd -= 1
        if cd > 0:
            continue
        else:
            cd = 10
        # 读取电量，写入显示


def reset():
    HW.write_byte_data(address, COMMAND_REGISTER, 0x00)
    HW.write_byte_data(address, COMMAND_REGISTER, 0x04)


def run():
    HW.write_byte_data(address, MODE_REGISTER, 0x40)
    HW.write_byte_data(address, MODE_REGISTER, 0x00)


def getSOC():
    # Konfiguration des MAX17043
    MSB = HW.read_byte_data(address, SOC_REGISTER)
    LSB = HW.read_byte_data(address, SOC_REGISTER)

    global value
    value = MSB + LSB / 256.0
