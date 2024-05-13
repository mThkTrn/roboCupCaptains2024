import sensor, image, time, math
import time
from pyb import UART
startTime1=0
x=0
y=0
uart = UART(3, 115200, timeout_char=1000)
uart.init(57600, bits=8, parity=None, stop=1, timeout_char=1000)
threshold_index = 0

thresholds = [(66, 76, 37, 59, 5, 31)] #ball
thresholds2 = [(42, 55, -41, -2, -29, -3)] #blue
thresholds3 = [(57, 76, -11, 13, 9, 52)] #yellow

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()
while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs = []
    #blobs2 = []
    x, y, xVel, yVel, balltheta = 0, 0, 0,
    for blob in img.find_blobs([thresholds[threshold_index]],pixels_threshold=10, area_threshold=10, merge=True):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        newX = blob.cx() - 160
        newY = 120 - blob.cy()
        distance = math.sqrt(newX*newX + newY*newY)
        a = -522.0
        b = 46.95
        c = -1.582
        d = 0.02583
        ee = -0.0002041
        f = 6.307*(10**(-7))
        formula = (a) + b*distance+ c*(distance**2) + d*(distance**3) + ee*(distance**4) + f*(distance**5);
        formula/=100
        balltheta=(math.atan2(-blob.cy()+120,blob.cx()-160)+math.pi);
        balltheta=2*math.pi-balltheta
        newX=math.cos(balltheta)*formula
        newY=math.sin(balltheta)*formula
        xVel=(newX-x)/(time.ticks()/1000-startTime1)
        yVel=(newY-y)/(time.ticks()/1000-startTime1)
        x=newX
        y=newY
        startTime1=time.ticks()/1000
    uart.write(str(x)+","+str(y)+","+str(xVel)+","+str(yVel)+","+str(balltheta)+"\n")

    currentblobs = img.find_blobs([thresholds2[threshold_index]],pixels_threshold=50, area_threshold=50, merge=True)
    biggestBlob = 0;
    for blob in img.find_blobs([thresholds2[threshold_index]],pixels_threshold=40, area_threshold=40, merge=True):
        if(biggestBlob==0):
            biggestBlob=blob
        print(currentblobs);
        print("blob count", blob.count())
        if(blob.area()> biggestBlob.area()):
            biggestBlob=blob
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        newX = blob.cx() - 160
        newY = 120 - blob.cy()
        distance = math.sqrt(newX*newX + newY*newY)
        a = -522.0
        b = 46.95
        c = -1.582
        d = 0.02583
        ee = -0.0002041
        f = 6.307*(10**(-7))
        print(biggestBlob)

    if biggestBlob == 0:
        bluetheta, formula = -1, -1

    bluetheta=(math.atan2(-biggestBlob.cy()+120,biggestBlob.cx()-160)+math.pi);
    bluetheta=2*math.pi-biggestBlob
    formula = (a) + b*distance+ c*(distance**2) + d*(distance**3) + ee*(distance**4) + f*(distance**5);
    uart.write("blue"+","+str(formula)+","+str(bluetheta)+"\n")

    currentblobsYel = img.find_blobs([thresholds3[threshold_index]],pixels_threshold=50, area_threshold=50, merge=True)
    biggestBlobYel = 0;
    for blob in img.find_blobs([thresholds3[threshold_index]],pixels_threshold=50, area_threshold=50, merge=True):
        if(biggestBlobYel==0):
            biggestBlobYel=blob
        print(currentblobsYel)
        if(blob.area()> biggestBlobYel.area()):
            biggestBlobYel=blob
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        newX = blob.cx() - 160
        newY = 120 - blob.cy()
        distance = math.sqrt(newX*newX + newY*newY)
        a = -522.0
        b = 46.95
        c = -1.582
        d = 0.02583
        ee = -0.0002041
        f = 6.307*(10**(-7))
        print(biggestBlobYel)

    if biggestBlobYel == 0:
        yellowtheta, formula = -1, -1

    yellowtheta=(math.atan2(-biggestBlobYel.cy()+120,biggestBlobYel.cx()-160)+math.pi)
    yellowtheta=2*math.pi-yellowtheta
    formula = (a) + b*distance+ c*(distance**2) + d*(distance**3) + ee*(distance**4) + f*(distance**5);
    print("yellow camera distance: ", distance, "yellow actual distance: ", formula, "theta", yellowtheta)
    uart.write("yellow"+","+str(formula)+","+str(yellowtheta)+"\n")
"""
    for blob in img.find_blobs([thresholds3[threshold_index]],pixels_threshold=150, area_threshold=150, merge=True):
        blobs2.append(blob)
        area = 0
    for blob in blobs2:
        if blob.area() > area2:
            area2 = blob.area()
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            newX = blob.cx() - 160
            newY = 120 - blob.cy()
            distance = math.sqrt(newX*newX + newY*newY)
            a = -522.0
            b = 46.95
            c = -1.582
            d = 0.02583
            ee = -0.0002041
            f = 6.307*(10**(-7))
            formula = (a) + b*distance+ c*(distance**2) + d*(distance**3) + ee*(distance**4) + f*(distance**5);
            print("blue camera distance: ", distance, "blue actual distance: ", formula)
"""
