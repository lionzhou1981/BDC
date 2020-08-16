import _thread
import time
import os
import smbus
import datetime
import Common


class Battery:
    def __init__(self):
        self.MAX17043_ADDR = 0x36
        self.MAX17043_VCELL = 0x02
        self.MAX17043_SOC = 0x04
        self.MAX17043_MODE = 0x06
        self.MAX17043_VERSION = 0x08
        self.MAX17043_CONFIG = 0x0c
        self.MAX17043_COMMAND = 0xfe
        self.VOLTAGE_MAX = 3900
        self.VOLTAGE_MIN = 3600
        self.bus = smbus.SMBus(1)
        self.voltage = -1
        self.percent = -1
        _thread.start_new_thread(Run, ())
        print("Battery Started.")

    def __del__(self):
        print("Battery Stopped")

    def Run(self):
        cd = 10
        while Common.RUNNING:
            time.sleep(0.1)
            if cd > 0:
                cd -= 1
                continue
            cd = 10
            self.voltage = self.readVoltage()
            self.percent = self.readPercentage()
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    def readVoltage(self):
        return (1.25 * (self.read16(self.MAX17043_VCELL) >> 4))

    def readPercentage(self):
        tmp = self.read16(self.MAX17043_SOC)
        return ((tmp >> 8) + 0.003906 * (tmp & 0x00ff))

    def write16(self, reg, dat):
        buf = [dat >> 8, dat & 0x00ff]
        self.bus.write_i2c_block_data(self.MAX17043_ADDR, reg, buf)

    def read16(self, reg):
        buf = self.bus.read_i2c_block_data(self.MAX17043_ADDR, reg, 2)
        return ((buf[0] << 8) | buf[1])

    def writeRegBits(self, reg, dat, bits, offset):
        tmp = self.read16(reg)
        tmp = (tmp & (~(bits << offset))) | (dat << offset)
        self.write16(reg, tmp)
