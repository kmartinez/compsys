#!/usr/bin/env python3
# simple web server on a Pi demo for comp1313
# requires Bottle and our adc.py helper
from bottle import route, run, template, redirect, response
import RPi.GPIO as GPIO
from time import sleep
import adc
import os
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# this sets up a web server on port 8080. 
# Access it with a web browser at http://YourPiIP:8080
# or on the Pi's web browser at http://localhost:8080
# makes these resources:
# /ledflash  - flashes red led
# /hello  - says hello world and arg if given like /hello/kirk
# /adc    - adc reading of channel 0
# /cputemp - temperature of CPU
# /ledswitch
# /graph - plot some adc values
LED = 13
led_state = False
measurements = []

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

@route('/ledswitch', method=['GET', 'POST'])
def index(name='ledswitch'):
    global led_state
    if led_state:
        GPIO.output(LED, GPIO.LOW)
        led_state = False
    else:
        GPIO.output(LED, GPIO.HIGH)
        led_state = True

    #make a HTML page with button to toggle LED
    led_status = "ON" if led_state else "OFF"
    return '''
        <h1>LED is currently: {} </h1>
        <form action="/ledswitch" method="post">
            <button type="submit">Toggle LED</button>
        </form>
    '''.format(led_status)

# thus makes a url /adc which returns the adc reading
@route('/adc')
def index(name='adc'):
    return '<p> %s</p>' % adc.get_ain(0)

@route('/cputemp')
def index(name='cputemp'):
    temp = os.popen("vcgencmd measure_temp").readline()
    return(temp)

@route('/sysinfo')
def index(name='sysinfo'):
    info = os.popen("neofetch --off | grep Memory").readline()
    return(info)

def generate_plot():
    # plot the data
    global measurements
    plt.figure()
    plt.plot(measurements, color='b', label='Measurements')
    plt.title("plot of ADC values")
    plt.xlabel("Measurement number")
    plt.ylabel("ADC value")
    plt.legend()

    # save plot data as BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return buf

@route('/plot.png')
def plot_image():
    buf = generate_plot()
    # say what mime type our data is
    response.content_type = 'image/png'
    return buf.getvalue()

@route('/graph')
def display_plot():
    global measurements
    # grab new measurements from adc and add to existing array
    for num in range(1,10):
        measurements.append(adc.get_ain(0))
    return '''
        <h1>ADC values</h1>
        <img src="plot.png" alt="Measurements Graph">
        <form action="/graph" method="get">
            <button type="submit">Update Graph</button>
        </form>
    '''

run(host='0.0.0.0', port=8080)
