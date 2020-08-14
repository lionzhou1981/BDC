import _thread
import time
import os
import smbus
import datetime
import Common

MAX17043_ADDR = 0x36
MAX17043_VCELL = 0x02
MAX17043_SOC = 0x04
MAX17043_MODE = 0x06
MAX17043_VERSION = 0x08
MAX17043_CONFIG = 0x0c
MAX17043_COMMAND = 0xfe
VOLTAGE_MAX = 3900
VOLTAGE_MIN = 3600

bus = smbus.SMBus(1)
voltage = -1
percent = -1


def Start():
    _thread.start_new_thread(Run, ())
    print("Battery Started.")


def Stop():
    print("Battery Stopped")


def Run():
    global voltage
    global percent
    cd = 10
    while Common.RUNNING:
        time.sleep(0.1)
        cd -= 1
        if cd > 0: continue
        else: cd = 10

        voltage = readVoltage()
        percent = readPercentage()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        log = "{0} : {1} - {2}".format(now, voltage, percent)
        f1 = open('/home/pi/battery.log', 'a')
        f1.write(log + "\n")
        f1.close()
        print(log)


def readVoltage():
    return (1.25 * (read16(MAX17043_VCELL) >> 4))


def readPercentage():
    tmp = read16(MAX17043_SOC)
    return ((tmp >> 8) + 0.003906 * (tmp & 0x00ff))


def write16(reg, dat):
    buf = [dat >> 8, dat & 0x00ff]
    bus.write_i2c_block_data(MAX17043_ADDR, reg, buf)


def read16(reg):
    buf = bus.read_i2c_block_data(MAX17043_ADDR, reg, 2)
    return ((buf[0] << 8) | buf[1])


def writeRegBits(reg, dat, bits, offset):
    tmp = read16(reg)
    tmp = (tmp & (~(bits << offset))) | (dat << offset)
    write16(reg, tmp)
