import RPi.GPIO as GPIO
from time import sleep

switchpin = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchpin, GPIO.IN)

def read_switch():
    return GPIO.input(switchpin)
    
while True:
    print(read_switch())
    sleep(1)
