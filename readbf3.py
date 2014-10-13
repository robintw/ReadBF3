import logging
import time
import sys

import serial


# Old sjinn code
# sjinn -d /dev/ttyUSB0 -b9600 -p8n1 -s "\r"
# sjinn -d /dev/ttyUSB0 -b9600 -p8n1 -s "S\r" -r20



def read_bf3(port):
    ser = serial.Serial(port, timeout=1)
    logging.info("Initiated communication")
    time.sleep(0.5)
    # Send a Unix-style newline to get it to wake up
    ser.write("\r")
    logging.info("Reading data")
    # Send S, followed by Unix-style newline to get data
    ser.write("S\r")
    # Get the data
    data = ser.readlines()
    # Remember to close the serial port or we'll have problems!
    ser.close()

    return data

if __name__ == '__main__':
    read_bf3(sys.argv[1])