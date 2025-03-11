#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
lm = Motor(Port.X)
rm = Motor(Port.Y)
wd = wheel_diameter=?
at = axle_track=?
robot = DriveBase(lm, rm, wd, at)

# Write your program here.
"""
while True: 
    # While True make the code runs forever
    if Button.CENTER in ev3.buttons.pressed():
    #the CENTER tells that is the button in the center in the brick
        robot.straight(-200)
        # the robot went 200mm backwards
    elif Button.RIGHT in ev3.buttons.pressed():
        ...
    else:
        robot.turn(1000)
        # if the center button wasnt pressed, the robot will turn 1000 degrees in the clockwise forever until the button be pressed.

"""

while robot.distance()  > -500:
    robot.drive(-200,0)
robot.stop()
lm.brake()
rm.brake()
wait(2000)
robot.turn(200)
# this code will make the robot drive backwards for 200mm/sec until it pass 500mm then the robot will stop and wait 2000ms (2sec) and turn 200deg.


