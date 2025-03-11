from functions.py import *
from imports.py import *

speed = 150
turn = 0

while True:
    robot.drive(speed, turn)
    if scor.color() == Color.GREEN:
        robot drive(speed,tur)
    elif scor.color() == Color.YELLOW:
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

dfdsfdsafdsafdsfd


