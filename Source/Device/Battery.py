import _thread
import time
import Common


def Run():
    _thread.start_new_thread(Loop, ())
    print("Battery {0}".format(Common.RUNNING))


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
