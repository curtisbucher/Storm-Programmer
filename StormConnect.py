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

## ASCII control bytes
START = b'\x12' #Start
END = b'\x13' #End
ENQ = b'\x15' # Enquire
ACK = b'\x16' #Acknowledge
CON1 = b'\x21' #Control 1
CON2 = b'\x22' #Control 2
CON3 = b'\x23' #Control 3
ESC = b'\x2b' # Escape

def write():
    ## Getting file to write from. Data is a long string of hex characters
    filename = input("File: ")
    with open(filename, "r") as f:
        data = f.read()
    
    #Converting to list of decimal numbers
    data = [int(d,16) for d in data]
    
    print("Writing " + str(len(data)) + " bytes to ROM from " + filename + "...\n")

    #Initiating Connection
    ser.write(START)
    
    #Sending data packets, 9 bytes at a time, ending with control
    for x in range(0,len(data),9):
        print(data[x:x+9])
        ser.write(data[x:x+9])
        ser.write(b'\t')
        
        if ser.read() != ACK: raise ConnectionError("Connection Disrupted")
        
    #Sending last bit of data
    ser.write(data[x:])
    ser.write(b'\t')
    if ser.read() != ACK: raise ConnectionError("Connection Disrupted")
    
    #Ending write cycle
    ser.write(END)

def byteRead():
    
    ser.write(int(input("Address: ")))
    byte = ser.read()
    
    ser.write(ESC)
    ser.read()
    print(int(byte))

def pageRead():
    incoming = []
    ser.write(START)
    
    while True:
        received = ser.read()
        
        if received == END:
            break
        
        if received != b'\t':
            incoming += received##_until(terminator = b'\t')
            
        #ser.write(ACK)
        

    print(incoming)
        
        
    
    

## Creating Serial Connection
ser = serial.Serial('/dev/cu.usbmodem14101')
time.sleep(2)
#os.system("clear")
print("LightningStorm 0.2.0")
print("--------------------")

## Establishing Connection
print("Connecting...")
ser.write(ENQ)
if ser.read() != ACK:
    raise ConnectionError("Connection Refused")
print("Connected!\n")

## Getting user request
user_in = input("Read/Write: ")
if user_in.lower() == "read":
    
    user_in = input("Byte Read or Page Read: ")
    if "byte" in user_in.lower():
        ser.write(CON2)
        ser.read()
        byteRead()
    elif "page" in user_in.lower():
        ser.write(CON1)
        ser.read()
        pageRead()

elif user_in.lower() == "write":
    ser.write(CON3)
    ser.read()
    write()
    
print("\n")


ser.close()

