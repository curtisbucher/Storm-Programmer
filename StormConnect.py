import serial
import os
VERSION = "0.1.0"

## Starting Serial Connection
ser = serial.Serial('/dev/cu.usbmodem14101')

ser = serial.Serial()
def print_header():
    os.system("clear")
    print("\nStorm Connect Version " + VERSION)
    print("---------------------------")
    
def write():
    """ User process for writing to ROM"""
    print_header()
    
    ## Getting Data From File
    filename = input("File: ")
    with open(filename, "r") as f:
        data = f.read()
    
    ## Viewing Data
    user_input = input("View Data (y,n): ")
    if user_input.lower() == "y":
        print_header()
        print("File: " + filename, end = "\n\n")
        print(data)
        input("Press [ENTER] to escape")
        print_header()
        
    ## Writing Data to RO
    user_input = input("Write to ROM (y,n): ")
    if user_input.lower() == "y":
        write_to_ROM(data)

def write_to_ROM(data):
    """ Writes raw data to ROM through serial arduino connection"""
    print_header()
    print("File: " + filename, end = "\n\n")
    
    print("Sending " + str(len(data)) + "kbytes...")
    ## Iterating through bytes in file
    for d in data():
        ## Sending Byte
        ser.write(d)
        ## Checking if confirmation byte is same as sent byte
        if ser.read() != d:
            print("Error: Attempting to Resend")
            write_to_ROM(data)
    ## Closing connection
    ser.sendBreak()
    print("Finished Writing! Read to Confirm")

def read():
    pass
    
    

print_header()
userInput = input("Read or Write: ")

if userInput.lower() == "read":
    pass
    ##read()
    
elif userInput.lower() == "write":
    pass
    write()

else:
    print("Error: Command not recognized")
    
ser.clost()
os.system("clear")