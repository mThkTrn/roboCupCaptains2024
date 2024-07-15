import serial_read as sr
import time

while True:
    sr.parse_serial()
    if sr.ballsize == -1:
        print("ball not seen")
    else:
        print("ball in view")
