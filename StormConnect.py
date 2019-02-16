#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 23:47:20 2019

@author: curtisbucher
Reset Arduino before each use. Wait for light to finish flashing
"""
import serial
import time
import os

POS = '/x01'
NEG = '/x00'
BUFF = 8 ## Buffer length. Size of transmissions

def read(start_addr, end_addr, buffer_size, file):
    """Commanding arduino to read data to `file` from ROM from [start_addr]
    to [end_addr].
    """
    ser.write(POS, start_addr, end_addr, buffer_size)
    
    ## Receiving data from arduino. The size of each transmission is sent in
    ## first byte.
    received = []
    while len(received < start_addr - end_addr):
        message_length = ser.read()
        received += ser.read(len=message_length)
        
        ## Indicating that the CPU is ready or more data
        ser.write(POS)
    
    ## Writing received data to file
    with open(file, "w") as data:
        data.write(received)

def write(start_addr, end_addr, buffer_size, file):
    """Commanding arduino to write data from `file` into ROM from [start_addr]
    to [end_addr].
    """
    
    ser.write(NEG, start_addr, end_addr, buffer_size)
    
    ## Reading data from file to write to ROM
    with open(file, "r") as d:
        data = d.read()
        
    ## Sending data in `buffer-size` peices, each with a header to
    ## indicate message size
    while len(data) > buffer_size:
        ser.write(buffer_size)
        ser.write(data[-buffer_size:])
        
        ## Indicating that the arduino is ready for more data
        ser.read()
    
    ## Sending the last little bit let over
    ser.write(len(data))
    ser.write(data)



## Creating Serial Connection
ser = serial.Serial('/dev/cu.usbmodem14101')
time.sleep(2)


os.system("clear")
print("LightningStorm 0.2.0")
print("--------------------")

## Establishing Connection
print("Connecting...")
ser.write(POS)
if ser.read() != POS:
    raise ConnectionError("Connection Refused")
print("Connected!\n")

## Getting user request
operation = input("Read/Write: ")
start_addr = input("Start Address: ")
end_addr = input("End Address: ")

if "read" in operation.lower():
    filename = input("File to read to: ")
    read(start_addr, end_addr, BUFF)

elif "write" in operation.lower():
    filename = input("File to write from: ")
    write(start_addr, end_addr, BUFF)

print("\n")
ser.close()

