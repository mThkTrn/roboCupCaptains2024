#WARNING: COde not updated to most recent version

import time
import math
import serial

ser = serial.Serial(115200)

from adafruit_motorkit import MotorKit

kit = MotorKit()

def drive_motors(pwr):
    kit.motor1.throttle = pwr[1]
    kit.motor2.throttle = pwr[2]
    kit.motor3.throttle = pwr[3]
    kit.motor4.throttle = pwr[4]

def ang_to_pwr(ang):
    return (math.cos(ang), math.sin(ang), math.cos(ang), math.sin(ang))

def turn(dir):
    # 1 means clockwise, -1, means counterclockwise
    return (dir, -dir, dir, -dir)

while True:
    ang = ser.read(1)
    if ang != -1:
        drive_motors(ang_to_pwr(ang))
    else:
        drive_motors(turn(1))
