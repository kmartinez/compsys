#!/usr/bin/env python
# simple web server on a Pi demo for comp1203
# requires Bottle
from bottle import route, run
import RPi.GPIO as GPIO
from time import sleep
import adc
import os

# this sets up a web server on port 8080. 
# Access it with a web browser at http://YourPiIP:8080
# or on the Pi's web browser at http://localhost:8080
# makes these resources:
# /ledflash  - flashes red led
# /hello  - says hello world and arg if given like /hello/kirk
# /adc    - adc reading of channel 0
# /cputemp - temperature of CPU
LED = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# this sets up the url /hello/name which prints "Hello name" if requested
@route('/hello/:name')
@route('/hello')
def index(name='World'):
    return '<b>Hello %s!</b>' % name

# this defines a URL which flashes the LED once
@route('/ledflash')
def index(name='ledflash'):
    GPIO.output(LED, GPIO.HIGH)                                                   
    sleep(0.5)                                                             
    GPIO.output(LED, GPIO.LOW)                                                   

# thus makes a url /adc which returns the adc reading
@route('/adc')
def index(name='adc'):
    return '<p> %s</p>' % adc.get_ain(0)

@route('/cputemp')
def index(name='cputemp'):
    temp = os.popen("vcgencmd measure_temp").readline()
    return(temp)

run(host='0.0.0.0', port=8080)
