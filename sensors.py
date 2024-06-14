import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

switchpin = 7 # change

GPIO.setup(switchpin, GPIO.IN)

def read_switch():
    return GPIO.input(switchpin)

goal_heading = -1

def update_goal_heading():
    goal_heading = read_compass()

def read_compass():
    pass

def see_line():
    pass