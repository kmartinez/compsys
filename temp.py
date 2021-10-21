#!/usr/bin/env python  
#
# use thermistor+8k2ohm on adc, when warm light up red LED, else green
# ain(1) is CH2 on pin 2 of the MCP3008
# threshold has to be chosen by experiment

import adc
import RPi.GPIO as GPIO
from time import sleep

RED = 13
ORANGE = 19
GREEN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(ORANGE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

try:
    while True:
        t = adc.get_ain(1)

        print t
        if t > 800 :
            GPIO.output(RED,GPIO.LOW)
            GPIO.output(GREEN,GPIO.HIGH)
        else :
            GPIO.output(GREEN,GPIO.LOW)                                                    
            GPIO.output(RED,GPIO.HIGH)
        sleep(0.3)

# this catches when you stop the program to turn off LEDs
except KeyboardInterrupt:
    GPIO.cleanup()


