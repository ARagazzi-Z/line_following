from functions import *
from imports import *

speed = 150
turn = 0

while True:
    robot.drive(speed, turn)
    if lscor.color() == Color.GREEN:
        robot.rive(speed,turn)
    elif rcor.color() == Color.YELLOW:
        speed /= 2
        robot.drive(speed, turn)
    elif scor.color() == Color.RED:
        robot.stop()
        lm.brake()
        rm.brake()
        wait(2000)
        speed *= 2
        robot.straight(150)
        robot.stop()
        lm.brake()
        rm.brake()



