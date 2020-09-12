import _thread
import time
import os
import smbus
import datetime
from libs import Adafruit_I2C
import Common


class Battery(Adafruit_I2C):
    def __init__(self, debug=False, adr=0x40, bus=1):
        Adafruit_I2C.__init__(self, adr, bus, debug)
        Adafruit_I2C.writeList(self, 0x05, [0x0a, 0x00])
        self.VOLTAGE_MAX = 3900
        self.VOLTAGE_MIN = 3600
        self.VOLTAGE_CHARGING = 4100
        self.voltage = -1
        self.percent = -1
        _thread.start_new_thread(self.Run, ())
        print("Battery Started.")

    def __del__(self):
        print("Battery Stopped")

    def Run(self):
        cd = 0
        while Common.RUNNING:
            time.sleep(0.1)
            if cd > 0:
                cd -= 1
                continue
            cd = 10
            self.voltage = self.readVoltage()
            if self.voltage < self.VOLTAGE_MIN:
                self.percent = 1
            elif self.voltage > self.VOLTAGE_CHARGING:
                self.percent = 999
            elif self.voltage > self.VOLTAGE_MAX:
                self.percent = 100
            else:
                self.percent = (self.voltage - self.VOLTAGE_MIN) / (self.VOLTAGE_MAX - self.VOLTAGE_MIN) * 100
            Common.CurrentBattery = self.percent

    def get_voltage(self):
        __raw_data = Adafruit_I2C.readU16(self, 0x02, False)
        self.voltage = __raw_data * 1.25 / 1000.0
        return self.voltage
