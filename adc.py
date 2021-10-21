"""
    Provides an easy to use python interface to all the adc stuff
    Assumes Raspberry Pi with MCP3008 ADC
    originally adapted by Ed Crampin from https://pimylifeup.com/raspberry-pi-adc/
    2018 adaption By Laurie Kirkcaldy
    principle is the ADC channel  number is sent and the two bytes of reading received and decoded
"""

import spidev


spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=400000

def get_ain(adcnum):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        r = spi.xfer2([1,(8+adcnum)<<4,0])
        data = ((r[1]&3) << 8) + r[2]
        return data
        
