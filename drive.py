from adafruit_motorkit import MotorKit
import time
import math
import serial
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

ser = serial.Serial("/dev/ttyACM0", 9600)
print("running drive.py")

shootpin = 10

GPIO.setup(shootpin,  GPIO.OUT)

kit = MotorKit()

def setpwrs(p1, p2, p3, p4):
    kit.motor1.throttle = p1
    kit.motor2.throttle = p2
    kit.motor3.throttle = p3
    kit.motor4.throttle = p4

def drive_ang(ang):
    ang = math.radians(ang) + (5/4)*math.pi
    setpwrs(math.sin(ang), math.cos(ang), math.sin(ang), math.cos(ang))

def read_serial():
    out = ser.readline().decode()[2:-5]
    if isalpha(out):
        return out
    else:
        return float(out)

print("running!")

while True:
    shoot = False
    serial_in = read_serial()
    print(serial_in)
    if serial_in == "":
        continue
    elif serial_in == "turn":
        setpwrs(1, 1, 1, 1)
    elif serial_in == "shoot":
        shoot = True
    else:
        drive_ang(ang)
    GPIO.output(shootpin, shoot)

