#!/usr/bin/env python3

"""Live monitor for the arduino chinchilla room temperature monitor"""

import sys
import time
import serial


try:
    mon = serial.Serial('/dev/ttyUSB0', 115200)
    while True:
        line = mon.readline().decode('utf-8').strip()
        t = time.asctime(time.localtime(time.time()))
        (station, temp, humid, count) = line.split()
        station = station.strip("R")
        print(
            F"{t}: Station:{station} "
            F"Temperature: {temp} Humidity: {humid}"
        )
except KeyboardInterrupt:
    print("Cleaning up")
    mon.close()
    sys.exit(1)
except FileNotFoundError:
    print("/dev/ttyUSB0 does not exist. Please ensure the main station is on.")
    mon.close()
    sys.exit(1)
