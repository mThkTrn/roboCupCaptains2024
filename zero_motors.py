import time

from adafruit_motorkit import MotorKit

kit = MotorKit()

def setpwrs(p1, p2, p3, p4):
    scale = 0.5
    kit.motor1.throttle = p1*scale
    kit.motor2.throttle = p2*scale
    kit.motor3.throttle = p3*scale
    kit.motor4.throttle = p4*scale
    
setpwrs(0,0,0,0)
