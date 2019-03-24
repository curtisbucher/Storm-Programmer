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

POS = b'\x01'
NEG = b'\x00'

def read(start_addr, end_addr, file=None):
    """Commanding arduino to read data to `file` from ROM from [start_addr]
    to [end_addr].
    """
    ser.write([1, start_addr, end_addr])
    
    ## Receiving data from arduino. The size of each transmission is sent in
    ## first byte.
    received = ser.read(size = end_addr- start_addr)
        
    ## Indicating that the CPU is ready or more data
    ser.write(POS)
    
    ## Writing received data to file
    received_list = list(received)
    print("Data: ", received_list)
    
    ## Converting to hex to write to file
    received = [hex(x)[2:] for x in received]
    received = ' '.join(received)
    
    ##Converting to hex to write to file
    if file:
        with open(file, "w") as data:
            data.write(received)
            
    return received_list
def write(start_addr, end_addr, file):
    """Commanding arduino to write data from `file` into ROM from [start_addr]
    to [end_addr].
    """
    ser.write([0, start_addr, end_addr])
    
    ## Reading data from file to write to ROM
    with open(file, "r") as d:
        data = d.read()
        
    ## Converting from hex string to int list
    data = data.split(' ')
    data = [int(x,16) for x in data]
    data = data[0:end_addr - start_addr]
    
    ## Must be sent in batches of 64, then wait for conformation
    print("-" * (((end_addr-start_addr)//64)+1))
    for a in range(start_addr, end_addr-64, 64):
        ser.write(data[a:a+64])
        ser.read()
        print("*",end="")
        
    ser.write(data[a+64:end_addr])
    ser.read()
    print("*")
    
    ##Checking Data
    received = read(start_addr, end_addr)
    
    print("\nSuccess!", len(data), "bytes sent!")
    
    print("Sent:",data)
    
## Creating Serial Connection
ser = serial.Serial('/dev/cu.usbmodem14101')
time.sleep(2)

os.system("clear")
print("LightningStorm 0.3.0")
print("--------------------")

## Establishing Connection
print("Connecting...")
ser.write(POS)
if ser.read() != POS:
    raise ConnectionError("Connection Refused")
print("Connected!\n")

while True:
    ## Getting user request
    operation = input("Read/Write: ")

    if "read" in operation.lower():
        start_addr = int(input("Start Address: ")) ## Add support for 16 bit addressing
        end_addr = int(input("End Address: "))
        filename = input("File to read to: ")
        
        read(start_addr, end_addr, filename)
    
    elif "write" in operation.lower():
        start_addr = int(input("Start Address: ")) ## Add support for 16 bit addressing
        end_addr = int(input("End Address: "))
        filename = input("File to write from: ")
        
        write(start_addr, end_addr, filename)
        
    else:
        print("Ending...")
        break

print("\n")
ser.close()

