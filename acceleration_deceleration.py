from imports import *
from functions import *

strength = 10
dist = 1000
time = 0.035

robot.reset()

while True:
    if robot.distance() < abs(dist()) / 2:
        strength += 1
        robot.drive(strength, 0) 
        wait(time)
        if robot.distance() == abs(dist()) / 2:
            while robot.distance() != abs(dist()):
                strength -= 1
                robot.drive(strength, 0) 
            robot.stop()
            lm.brake()
            rm.brake()