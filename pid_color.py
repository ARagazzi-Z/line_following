from functions import *
from imports import *

kp = 25
# P (Proporcional): Multiplica o erro por kp para corrigir a direção.
ki = 0
# I (Integral): Acumula pequenos erros ao longo do tempo.
kd = 5
# D (Derivada): Reage a mudanças rápidas no erro para evitar oscilações.

last_error = 0
integral = 0
count = 0

while True:
    error = lscor.color() - rscor.color()
    P = error * kp
    integral += error
    I = integral * ki
    D = (error - last_error)* kd
    turn = P + I + D 
    
    last_error = error #atualiza o erro
    speed = 30 

    robot.drive(speed, turn)

    wait(10)

# LEITURA DO VERDE
    # 1 verde
    if (lscor.color() == Color.GREEN) != (rscor.color() == Color.GREEN):
        robot.drive(-40, 0)
        if lscor.color() == Color.BLACK or rscor.color() == Color.BLACK:
            count = 0
        else:
            count += 1
    else:
        count = 0

    if count == 10:
        if lscor.color() == Color.GREEN:
            while lscor.color() != Color.WHITE:
                robot.drive(20, 0)
            while rscor.color() != Color.BLACK:
                robot.turn(20, -10)
                count = 0
        elif rscor.color() == Color.GREEN:
            while rscor.color() != Color.WHITE:
                robot.drive(20, 0)
            while lscor.color() != Color.BLACK:
                robot.turn(20, 10)
                count = 0
    # beco sem saída
    if lscor.color() == Color.GREEN and rscor.color() == Color.GREEN:
        robot.drive(-40, 0)
        if lscor.color() != Color.BLACK and rscor.color() != Color.BLACK:
            robot.turn(20, 180)



