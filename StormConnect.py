#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 23:47:20 2019

@author: curtisbucher
Reset Arduino before each use. Wait for light to finish flashing
"""
import serial
import time


# Word header. Word = [header, byte]
COMMAND = b"\xff"  # Used to signal that the following byte is a command
DATA = b"\x00"  # Used to signal that the following byte is data

# Commands
NEG = b"\x00"  # Negetive
POS = b"\x01"  # Positive


def connect():
    ser.write(COMMAND + POS)
    received = ser.read(size=2)
    if received != COMMAND + POS:
        raise ConnectionError("Connection Refused")
    print("Connected!")


def writePage():
    pass


def readPage():
    pass


def writeByte():
    pass


def readByte():
    address = int(input("Address: "))
    ser.write(DATA)
    ser.write(address)
    ser.read()
    received = ser.read()
    print("Data at", address, ":",received)

# Creating Serial Connection
ser = serial.Serial("/dev/cu.usbmodem14101")
time.sleep(2)
# os.system("clear")
print("LightningStorm 0.2.0")
print("--------------------")

# Establishing Connection
print("Connecting...")
connect()

# Getting user request
user_in = input("Read/Write: ")
if user_in.lower() == "read":
    ser.write(COMMAND + NEG)
    user_in = input("Byte Read or Page Read: ")
    if "byte" in user_in.lower():
        ser.write(COMMAND + POS)
        ser.read(size=2)
        readByte()
    elif "page" in user_in.lower():
        ser.write(COMMAND + NEG)
        ser.read(size=2)
        readPage()

elif user_in.lower() == "write":
    ser.write(COMMAND + POS)
    user_in = input("Byte Write or Page Write: ")
    if "byte" in user_in.lower():
        ser.write(COMMAND + POS)
        ser.read(size=2)
        writeByte()
    elif "page" in user_in.lower():
        ser.write(COMMAND + NEG)
        ser.read(size=2)
        writePage()
print("\n")


ser.close()
