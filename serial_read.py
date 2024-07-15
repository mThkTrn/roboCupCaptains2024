import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

def read_serial():
    out = ser.readline().decode()
    return out
    

ballang, ballsize, goal1ang, goal1size, goal2ang, goal2size = -1, -1, -1, -1, -1, -1

def parse_serial():
    global ballang
    global ballsize
    global goal1ang
    global goal2size
    global goal2ang
    global goal2size
    cam_in = read_serial()
    #print("--")
    print(cam_in[:-1])
    if len(cam_in.split(",")) == 6:
        #print("updating values...")
        ballang, ballsize, goal1ang, goal1size, goal2ang, goal2size = [float(k) for k in cam_in.split(",")]
        #print(ballsize)
