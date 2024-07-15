import drivetrain as dt
import time

dt.setpwrs(1, 0, 0, 0)
time.sleep(2)
dt.setpwrs(0, 1, 0, 0)
time.sleep(1)
dt.setpwrs(0, 0, 1, 0)
time.sleep(1)
dt.setpwrs(0, 0, 0, 1)
time.sleep(2)
dt.turn(0.5)
time.sleep(1)
dt.setpwrs(1, 0, -1, 0)
dt.setpwrs(0, 0, 0, 0)

#dt.setpwrs(1, 1, 1, 1)
#time.sleep(3)
#dt.setpwrs(0, 0, 0, 0)
