import drivetrain as dt
import serial_read as sr
import time

start_time = time.time()*10

while True:
	sr.parse_serial()
	print(sr.ballsize)
	if sr.ballsize == -1:
		if (time.time()*10-start_time)%10 < 2:
			dt.turn(0.8)
		else:
			dt.turn(0)
	else:
		dt.setpwrs(-1, 1, -1, 1)
