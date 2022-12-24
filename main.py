#!/usr/bin/python3

from monitor import Monitor
from time import sleep

monitor = Monitor()

while 1:
    if monitor.isOnBattery():
        print(monitor.getTimeOnBattery())
    sleep(1)