#!/usr/bin/env python3  
#
# print an adc value using our adc helper function
# get_ain(chanum) where chanum 0 for CH0 on MCP3008 etc

import adc
from time import sleep

while True:
    print(adc.get_ain(0))
    sleep(0.3)

