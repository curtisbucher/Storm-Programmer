#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 23:47:20 2019

@author: curtisbucher
Reset Arduino before each use. Wait for light to finish flashing
"""
import serial
import time
try:
    ## Creating Serial Connection
    ser = serial.Serial('/dev/cu.usbmodem14101')
    ##ser.open()
    
    ## Creating data bytearray, cannot be larger than 10 due to buffer size. 
    data = (1,1,2,3,4,5,223,7,8,8)
    ##print(list(data))
    
    ## Sending Data
    time.sleep(2)
    print(ser.write(data[:10]))
    
    ## Receiving Data
    ser.timeout = 2
    incoming = ser.read_until(terminator = b'\t')
    
    print(list(incoming))
    ser.close()
    
except Exception:
    pass
    ser.close()
