#!/usr/bin/python
#import time
#import py_qmc5883l
#sensor = py_qmc5883l.QMC5883L()
#while True:
    #print(sensor.get_magnet())
    #print(sensor.get_bearing())
    #time.sleep(0.2)

import sensors as sn
import time

while True:
    sn.callibrate_compass()
    print(sn.get_heading_scaled())
    time.sleep(0.1)
