import time
import math
import board
import py_qmc5883l
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

sensor = py_qmc5883l.QMC5883L()

max_compass_val = 0
min_compass_val = 360

def num_to_range(num, inMin, inMax, outMin, outMax):
    try:
        return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
    except ZeroDivisionError:
        return num

num_to_range(5, 0, 10, 0, 100) # 50.0

def get_heading_raw():
    return sensor.get_bearing()

def get_heading_scaled():
    return num_to_range(get_heading_raw(), min_compass_val, max_compass_val, 0, 360)

switchpin = 16 # change

GPIO.setup(switchpin, GPIO.IN)

def read_switch():
    return GPIO.input(switchpin)

goal_heading = -1

def update_goal_heading():
    goal_heading = get_heading_scaled()


def callibrate_compass():
    global max_compass_val
    global min_compass_val
    val = get_heading_raw()
    if val > max_compass_val:
        max_compass_val = val
    if val < min_compass_val:
        min_compass_val = val


def on_line():
    pass
