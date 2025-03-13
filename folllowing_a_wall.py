from functions import *
from imports import *

while True:
    if ultras.distance() < 100:
        # if the ultrassonic sensor is reading a distance that is less than 10cm (100mm) 
        # so the robot will drive in a speed of 100mm/sec and turning 30 degrees in the counterclockwise
        robot.drive(100, -30)
    else:
        #in any other case the robot will drive at the same speed but now turning at the opposite direction, 30 degrees in the clockwise
        robot.drive(100, 30)

         
