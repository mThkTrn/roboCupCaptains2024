#WARNING: Code not updated to most recent version

import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import image # Import module containing machine vision algorithms
import time # Import module for tracking elapsed time
import math


sensor.reset() # Resets the sensor
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px
sensor.skip_frames(time = 2000) # Skip some frames to let the image stabilize

goalminsize = 10

# Define thresholds
thresholdsBall = (0, 100, 19, 127, -128, 127)
goal1thresholds = (73, 100, -128, 42, -128, 40) #blue
goal2thresholds = (73, 100, -128, 42, -128, 40) #yellow

ledRed = pyb.LED(1) # Initiates the red led
ledGreen = pyb.LED(2) # Initiates the green led

clock = time.clock() # Instantiates a clock object

ang = 0
targetgoal = -1

while True:
    clock.tick() # Advances the clock
    img = sensor.snapshot() # Takes a snapshot and saves it in memory

    ballcoords = [-1,-1]
    goal1coords = [-1, -1]
    goal2coords=[-1,-1]
    ballsize = -1
    goal1size = -1
    goal2size = -1
    # Draw blobs

    blobs = img.find_blobs([thresholdsBall], merge=True)

    for blob in blobs:
        if blob.area() > ballsize:
            img.draw_rectangle(blob.rect(), color=(255,0,0))
            ballcoords = [blob.cx(), blob.cy()]
            img.draw_cross(blob.cx(), blob.cy(), color=(255,0,0))
            ballsize = blob.area()

    #Turn on green LED if a blob was found
    if len(blobs) > 0:
        ledGreen.on()
        ledRed.off()
    else:
    # Turn the red LED on if no blob was found
        ledGreen.off()
        ledRed.on()

    goal1blobs = img.find_blobs([goal1thresholds], merge=True)
    for blob in goal1blobs:
        # Draw a rectangle where the blob was found
        if blob.area() > goalminsize and blob.area() > goal1size:
            img.draw_rectangle(blob.rect(), color=(0,0,255))
            goal1coords = [blob.cx(), blob.cy()]
            # Draw a cross in the middle of the blob
            img.draw_cross(blob.cx(), blob.cy(), color=(0,0,255))
            goal1size = blob.area()

    goal2blobs = img.find_blobs([goal1thresholds], merge=True)
    for blob in goal2blobs:
        # Draw a rectangle where the blob was found
        if blob.area() > goalminsize and blob.area() > goal2size:
            img.draw_rectangle(blob.rect(), color=(0,255,255))
            goal2coords = [blob.cx(), blob.cy()]
            img.draw_cross(blob.cx(), blob.cy(), color=(0,255,255))
            goal2size = blob.area()

    pyb.delay(50) # Pauses the execution for 50ms
    center = (160, 240)

    ballvec = [ballcoords[0]-center[0], ballcoords[1]-center[1]]
    goal1vec = [goal1coords[0]-center[0], goal1coords[1]-center[1]]
    goal2vec = [goal2coords[0]-center[0], goal2coords[1]-center[1]]

    if ballvec !+ [-1, -1]:
        try:
            ballang = math.atan(ballcoords[1]/ballcoords[0])
        except ZeroDivisionError:
            ballang = -10 # -10 is the code for straight ahead
    else:
        ballang = -1

    if goal1vec != [-1, -1]:
            try:
                goal1ang = math.atan(goal1coords[1]/goal1coords[0])
            except ZeroDivisionError:
                goal1ang = -10 # -10 is the code for straight ahead
    else:
        goal1ang = -1
    

    if goal2vec != [-1, -1]:
        try:
            goal2ang = math.atan(goal2coords[1]/goal2coords[0])
        except ZeroDivisionError:
            goal2ang = math.pi/2
    else:
        goal2ang = -1

    print(f"{ballang}, {ballsize}, {goal1ang}, {goal1size}, {goal2ang}, {goal2size}")