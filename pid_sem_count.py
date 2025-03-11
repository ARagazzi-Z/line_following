from functions.py import *
from imports.py import *

kp = 3
ki = 0
kd = 0
last_error = 0
integral = 0

while True:
    error = lscor.reflection() - rscor.reflection() 
    P = error * kp
    I = (error + integral)* ki
    D = (error - last_error)* kd
    turn = P + I + D 
    
    last_error = error #atualiza o erro
    speed = 30 

    robot.drive(speed, turn)

    wait(10)

    if lscor.color() == Color.GREEN:
        robot.turn(-90)
        robot.drive(speed, turn)
    else:
        robot.drive(speed, turn)
            
    if rscor.color() == Color.GREEN:
        robot.turn(90)
        robot.drive(speed, turn)
    else:
        robot.drive(speed, turn)

        
