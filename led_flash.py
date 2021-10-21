#!/usr/bin/env python3
# this example only flashes the red LED on output 13
import RPi.GPIO as GPIO
import os
from time import sleep

delay = 0.1
LED = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED,GPIO.HIGH)
        sleep(delay)
        GPIO.output(LED,GPIO.LOW)
        sleep(delay)
        
except KeyboardInterrupt:
    GPIO.cleanup()
