import drivetrain as dt
import time
import math
# this program should first move forward, then at 90 degrees, 180 degrees and 27 degrees, each for one second. It will then spin counterclockwise, annd then clockwise, each for one second

dt.drive_ang(0)
time.sleep(1)
dt.drive_ang(math.pi/2)
time.sleep(1)
dt.drive_ang(math.pi)
time.sleep(1)
dt.drive_ang(3*math.pi/2)
time.sleep(1)
dt.spin(0.1)
time.sleep(1)
dt.spin(-0.1)
time.sleep(1)
dt.zero_motors()
