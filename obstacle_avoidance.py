from functions import *
from imports import *
from gyro_turn import gyro_90, gyro_90neg

if ultras.distance() <= 40:
    robot.straight(-20)
    gyro_90()
    robot.straight(80)
    gyro_90()
    robot.straight(200)
    gyro_90()
    robot.straight(80)
    gyro_90neg()



    