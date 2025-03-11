from functions.py import *
from imports.py import *

robot = DriveBase(lm, rm, wd, at)
light = ColorSensor(Port.SX)

Distance = 1000
reflection = 30
LFPK = 2
# LFPK = Line Following Proportional Constant
speed = 150

# Write your program here.
while robot.distance() >= Distance:
    correction = (reflection - light.reflection())*LFPK
    #correction is the reflection between the white and black, in this case for Zain (youtube) is 30 - the light reflection of the moment. 
    #correction is just (BLACK reflection + WHITE reflection) / 2.  
    robot.drive(speed, correction)
    #line following works with a lower value
    #250 is the speed in mm, so 250mm/sec is 25cm 
robot.stop()
lm.brake()
rm.brake()


