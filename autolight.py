#!/usr/bin/env python3
# turn on LED if it is dark
# use LDR with adc for input and a gpio to an LED
# the threshold level of 800 will need adjusting
# the principle is that the LDR increases in resistance in the dark, the circuit drops in voltage, ADC value drops
import RPi.GPIO as GPIO
import adc
from time import sleep

LED = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

threshold = 800
# turn on the light if its dark
try:
	while True:
	    value = adc.get_ain(0)
	    print(value)
	    if value < threshold :
	        GPIO.output(LED,GPIO.HIGH)
	    else :
	        GPIO.output(LED,GPIO.LOW)
	    sleep(0.3)

# this catches when you stop the program to turn off LEDs
except KeyboardInterrupt:
    GPIO.cleanup()
