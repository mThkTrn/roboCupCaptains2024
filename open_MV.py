#WARNING: Code not updated to most recent version

import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import image # Import module containing machine vision algorithms
import time # Import module for tracking elapsed time
import math
import serial 
sensor.reset() # Resets the sensor
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px
sensor.set_vflip(True) # Flips the image vertically
sensor.set_hmirror(True) # Mirrors the image horizontally
sensor.skip_frames(time = 2000) # Skip some frames to let the image stabilize

ser = serial.Serial(115200)

# Define the min/max LAB values we're looking for for the ball
thresholdsBall = (73, 100, -128, 42, -128, 40)
goal1thresholds = (73, 100, -128, 42, -128, 40) #change thresholds
goal2thresholds = (73, 100, -128, 42, -128, 40) #change thresholds

ledRed = pyb.LED(1) # Initiates the red led
ledGreen = pyb.LED(2) # Initiates the green led

clock = time.clock() # Instantiates a clock object

while(True):
    clock.tick() # Advances the clock
    img = sensor.snapshot() # Takes a snapshot and saves it in memory

    # Find blobs with a minimal area of 50x50 = 2500 px
    # Overlapping blobs will be merged
    blobs = img.find_blobs([thresholdsBall], area_threshold=2, merge=True)

    ballcoords = [-1,-1]
    goalcoords = 
    # Draw blobs
    for blob in blobs:
        # Draw a rectangle where the blob was found
        if blob.area() > 100 and blob.area() < 1000:
            img.draw_rectangle(blob.rect(), color=(0,255,0))
            ballcoords = [blob.cx(), blob.cy()]
            # Draw a cross in the middle of the blob
            img.draw_cross(blob.cx(), blob.cy(), color=(0,255,0))

    # Turn on green LED if a blob was found
#    if len(blobs) > 0:
#        ledGreen.on()
#        ledRed.off()
#    else:
#    # Turn the red LED on if no blob was found
#        ledGreen.off()
#        ledRed.on()

    pyb.delay(50) # Pauses the execution for 50ms
    center = (169, 102)
    vector = [ballcoords[0]-center[0], ballcoords[1]-center[1]]
    ang = math.atan(vector[1]/vector[0])
    print(ballcoords, vector, ang) # Prints the framerate to the serial console
    ser.write(ang, 1, "little")