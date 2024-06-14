import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

def read_serial():
    out = ser.readline().decode()
    return out
    

ballang, ballsize, goal1ang, goal1size, goal2ang, goal2size = -1, -1, -1, -1, -1, -1

def parse_serial():
    ballang, ballsize, goal1ang, goal1size, goal2ang, goal2size = [int(k) for k in read_serial().split(",")]
