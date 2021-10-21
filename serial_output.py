#!/usr/bin/env python3
from sys import argv
from serial import Serial
from time import sleep

DEFAULT_STRING = "A"
PORT = "/dev/serial0"
BAUD = 9600

try:
    if len(argv) == 2:
        # argument has been passed to the program
        outstr = bytes(argv[1], 'ascii')
    else:
        outstr = bytes(DEFAULT_STRING, 'ascii')
    print("Outputing %s" % outstr)
    SERIAL_PORT = Serial(PORT, BAUD, timeout=0.1)
    while True:
        SERIAL_PORT.write(outstr)
        sleep(0.5)
except KeyboardInterrupt:
    SERIAL_PORT.close()
