from functions import *
from imports import *

light = ColorSensor(Port.SX)

"""
GYRO

while gyro.angle() < 90:
    robot.drive(250,10)
robot.stop()
lm.brake()
rm.brake()
print(gyro.angle())
    # this code tells that the robot must drive 10deg/sec in a speed of 250mm/sec until the accumulated angle(detected by the gyro) be greater than 90. 
    # Once the accumulated angle is greater than 90, the robot will stop and print the gyro's angle detection.

"""
#
"""

COLOR REFLECTION

while light.reflection() > 15:
    robot.drive(-100,0)
robot.stop()
lm.brake()
rm.brake()
# this code makes the robot drive backward (because the -100 speed) straight until it see a lower reflection, in this case a black line. 
# so when it see a black line it will stop.
# IT A WAY TO "IDENTIFY" A BLACK LINE

"""

while True:
    while light.reflection() > 15:
        robot.drive(-100,0)
    robot.stop()
    lm.brake()
    rm.brake()
    while light.reflection() < 50:
        robot.drive(100,0)
    robot.stop()
    lm.brake()
    rm.brake()
#the WHILE TRUE makes the code runs forever.
# inside of the WHILE TRUE, the 1st while makes a question to the color sensor and answer: 
# if the reflection of the surface is greater than 15 the robot will drive backward, 
# but if it is less than 15, the robot will stop.
    # in the real situation, the robot will drive until it detect a reflection that is less than 15, what is probably a black, so it will stop.
# when the 1st while condition fineshes, it will start to ask the 2nd while consition:
# if the reflection of the surface is less than 50 the robot will drive forward,
# but if it is greater than 50, the robot will stop.
    # in the real situation, the robot will drive until it detect a reflection that is greater than 50, what is probably white or a bright color, so it will stop.
    # and then it starts all again, because of the while true.

"""
IT A WAY TO FIND A WHITE AND BLACK LINE BY THE REFLECTION INTENSITY.
"""

    

    
