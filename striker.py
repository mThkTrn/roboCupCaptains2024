import serial_read as sr
import drivetrain as dt
import sensors as sn
import math

ball_bay_size = 100 # change
ball_close_size = 75 # change

goal_shoot_size = 150 # change

target_goal = -1

ang_threshold = math.pi/18
while True:

    drive_switch = sn.read_switch()

    if not drive_switch:
        if sr.goal1ang != -1 and target_goal = -1:
            target_goal = 1
        if sr.goal2ang != -1 and target_goal = -1:
            target_goal = 2
        
        sn.update_goal_heading()
    else:
        if sn.see_line:
            dt.drive_ang(math.pi)
        sr.parse_serial()
        if sr.ballang > math.pi/2 + ang_threshold:
            dt.turn(-0.1)
        elif sr.ballang < math.pi/2 - ang_threshold:
            dt.turn(0.1)
        elif sr.ballang == -1:
            dt.turn(0.1)
        else:
            if sr.ballsize > ball_bay_size:
                if target_goal == 1:
                    if sr.goal1ang == -1:
                        dt.turn(0.1)
                    else:
                        dt.drive_ang(0)
                elif target_goal == 2:
                    if sr.goal2ang == -1:
                        dt.turn(0.1)
                    else:
                        if (target_goal == 1 and sr.goal1size > goal_shoot_size) or (target_goal == 2 and sr.goal2size > goal_shoot_size):
                            dt.shoot()
                        else:
                           dt.drive_ang(0)
            elif sr.ballsize < ball_bay_size and sr.ballsize > ball_close_size:
                pass
            #implement fancy rotation in circle
            else:
                dt.drive_ang(0)


    