#!/usr/bin/env python
import RPi.GPIO as GPIO
import os

LED = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED,GPIO.HIGH)
        GPIO.output(LED,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()

