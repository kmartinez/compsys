#!/usr/bin/env python3
#
# flash LEDs in sequence
# Red = GPIO 13
# Orange/Blue = GPIO 19
# Green = GPIO 26 

import RPi.GPIO as GPIO
from time import sleep

RED = 13
ORANGE = 19
GREEN = 26
ontime = 0.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(ORANGE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)


try:
    while True:
        GPIO.output(RED,GPIO.HIGH)
        sleep(ontime)
        GPIO.output(RED,GPIO.LOW)
        GPIO.output(ORANGE,GPIO.HIGH)
        sleep(ontime)
        GPIO.output(ORANGE,GPIO.LOW)
        GPIO.output(GREEN,GPIO.HIGH)
        sleep(ontime)
        GPIO.output(GREEN,GPIO.LOW)

# this catches when you stop the program
except KeyboardInterrupt:
    GPIO.cleanup()
