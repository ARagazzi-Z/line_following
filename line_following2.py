from functions.py import *
from imports.py import *

robot = DriveBase(lm, rm, wd, at)
light = ColorSensor(Port.SX)
speed = 150
BLACK = 10
WHITE = 70
treshold = (BLACK + WHITE) / 2
kp = 1.2
while True:
    error = light.reflection() - treshold
    correction = error * kp
    robot(speed, correction)

