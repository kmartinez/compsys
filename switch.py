#!/usr/bin/env python3
#
# turn on the red LED when the switch is pressed
# put switch as shown in the lab diagram
# 
# Switch = GPIO 21
# LED = GPIO 13

import RPi.GPIO as GPIO
from time import sleep
SWITCH = 21
LED = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN)


try:
    while True:
        sw = GPIO.input(SWITCH)
        if sw :
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)

# this catches when you stop the program
except KeyboardInterrupt:
    GPIO.cleanup()
