from adafruit_motorkit import MotorKit
import time
import math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


shootpin = 10 # change

GPIO.setup(shootpin,  GPIO.OUT)

kit = MotorKit()

def setpwrs(p1, p2, p3, p4):
    kit.motor1.throttle = -p1
    kit.motor2.throttle = p2
    kit.motor3.throttle = -p3
    kit.motor4.throttle = p4

def drive_ang(ang):
    ang = math.radians(ang) + (5/4)*math.pi
    setpwrs(math.sin(ang), math.cos(ang), math.sin(ang), math.cos(ang))

def turn(speed):
    setpwrs(speed, speed, speed, speed)

def shoot():
    GPIO.output(shootpin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(shootpin, GPIO.LOW)

def zero_motors():
    setpwrs(0, 0, 0, 0)

#def circle():


# while True:
#     shoot = False
#     serial_in = read_serial()
#     print(serial_in)
#     if serial_in == "":
#         continue
#     elif serial_in == "turn":
#         setpwrs(1, 1, 1, 1)
#     elif serial_in == "shoot":
#         shoot = True
#     else:
#         drive_ang(ang)
#     GPIO.output(shootpin, shoot)
