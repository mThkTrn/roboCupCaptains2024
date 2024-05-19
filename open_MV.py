#WARNING: Code not updated to most recent version

import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import image # Import module containing machine vision algorithms
import time # Import module for tracking elapsed time
import math
sensor.reset() # Resets the sensor
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px
#sensor.set_vflip(True) # Flips the image vertically
#sensor.set_hmirror(True) # Mirrors the image horizontally
sensor.skip_frames(time = 2000) # Skip some frames to let the image stabilize


uart = pyb.UART(3, 9600, timeout_char=1000)
uart.init(9600)

goalminsize = 10
goalsize = -1
goalshootsize = 100

# Define the min/max LAB values we're looking for for the ball
thresholdsBall = (0, 100, 19, 127, -128, 127)
goal1thresholds = (73, 100, -128, 42, -128, 40) #change thresholds, blue
goal2thresholds = (73, 100, -128, 42, -128, 40) #change thresholds, yellow

ledRed = pyb.LED(1) # Initiates the red led
ledGreen = pyb.LED(2) # Initiates the green led

clock = time.clock() # Instantiates a clock object

ang = 0
targetgoal = -1

while(True):
    clock.tick() # Advances the clock
    img = sensor.snapshot() # Takes a snapshot and saves it in memory

    # Find blobs with a minimal area of 50x50 = 2500 px
    # Overlapping blobs will be merged


    ballcoords = [-1,-1]
    goal1coords = [-1, -1]
    goal2coords=[-1,-1]
    # Draw blobs

    blobs = img.find_blobs([thresholdsBall], merge=True)

    for blob in blobs:
        # Draw a rectangle where the blob was found
        #if blob.area() > 1 and blob.area() < 1000:
        img.draw_rectangle(blob.rect(), color=(255,0,0))
        ballcoords = [blob.cx(), blob.cy()]
        # Draw a cross in the middle of the blob
        img.draw_cross(blob.cx(), blob.cy(), color=(255,0,0))

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
        if blob.area() > goalminsize:
            if targetgoal == -1: targetgoal=1
            img.draw_rectangle(blob.rect(), color=(0,0,255))
            goal1 = [blob.cx(), blob.cy()]
            # Draw a cross in the middle of the blob
            img.draw_cross(blob.cx(), blob.cy(), color=(0,0,255))
            if targetgoal == 1:
                goalsize = blob.area()

    goal2blobs = img.find_blobs([goal1thresholds], merge=True)
    for blob in goal2blobs:
        # Draw a rectangle where the blob was found
        if blob.area() > goalminsize:
            if targetgoal == -1: targetgoal=2
            img.draw_rectangle(blob.rect(), color=(0,255,255))
            goal2 = [blob.cx(), blob.cy()]
            # Draw a cross in the middle of the blob
            img.draw_cross(blob.cx(), blob.cy(), color=(0,255,255))
            if targetgoal == 2:
                goalsize = blob.area()

    pyb.delay(50) # Pauses the execution for 50ms
    center = (160, 240)
    vector = [ballcoords[0]-center[0], ballcoords[1]-center[1]]
    if ballcoords == [-1, -1]:
        if targetgoal == 1:
            vector = [goal1coords[0]-center[0], goal1coords[1]-center[1]]
            if goalsize > goalshootsize:
                print("--shoot"+"\n")
        elif targetgoal == 2:
            vector = [goal2coords[0]-center[0], goal2coords[1]-center[1]]
            if goalsize > goalshootsize:
                print("--shoot"+"\n")
        else:
            print("--turn"+"\n")
    try:
        ang = math.atan(vector[0]/vector[1])
    except ZeroDivisionError:
        ang = math.pi
    #print(ballcoords, vector, ang) # Prints the framerate to the serial console
    #uart.write(ang, 1, "little")
    out = (str(ang)+"\n").encode("utf-8")
    print(out)
#    for i in list(map(hex, out)):

#        #uart.write(int(i).to_bytes(1, "little"))
#        print(int(i))
    #uart.write(int(50).to_bytes(1, "big"))

