from functions.py import *
from imports.py import *

kp = 1
# P (Proporcional): Multiplica o erro por kp para corrigir a direção.
ki = 0
# I (Integral): Acumula pequenos erros ao longo do tempo.
kd = 6.5
# D (Derivada): Reage a mudanças rápidas no erro para evitar oscilações.

last_error = 0
integral = 0
lcount = 0
rcount = 0

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

# LEITURA DO VERDE
    if lscor.color() == Color.GREEN:
        lcount += 1
    else:
        lcount = 0

    if rscor.color() == Color.GREEN:
        rcount += 1
    else:
        rcount = 0

    if lcount == 3:
        while lscor.color() != Color.WHITE:
            robot.drive(speed, 0)
        while rscor.color() != Color.BLACK:
            robot.turn(-10)
            lcount = 0
        
    if rcount == 3:
        while rscor.color() != Color.WHITE:
            robot.drive(speed, 0)
        while lscor.color() != Color.BLACK:
            robot.turn(10)
            rcount = 0

    