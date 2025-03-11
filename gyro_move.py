
from functions import *
from imports import *


kp = -1.7
ki = 0.
kd = -10

integral = 0
last_error = 0


# ref é a referência, o valor que quer chegar
# A EQUAÇÃO: Erro = [leitura do sensor] - [ref] 
def gyro_straight():
    while True:
        ref = 0 # andar reto
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
        
        last_error = error #atualiza o erro

        robot.drive(30, turn)


def mgyro_10():
    while True:
        ref = 10 
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
        
        last_error = error #atualiza o erro

        robot.drive(30, turn)


def mgyro_10neg():
    while True:
        ref = -10 
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
        
        last_error = error #atualiza o erro

        robot.drive(30, turn)
