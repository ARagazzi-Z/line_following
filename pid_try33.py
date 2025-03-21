from functions import *
from imports import *
from gyro_turn import gyro_180, gyro_90, gyro_90neg
from gyro_move import mgyro_10, mgyro_10neg


kp = 3
# P (Proporcional): Multiplica o erro por kp para corrigir a direção.
ki = 0
# I (Integral): Acumula pequenos erros ao longo do tempo.
kd = 6.5
# D (Derivada): Reage a mudanças rápidas no erro para evitar oscilações.

last_error = 0
integral = 0
count = 0
bcount = 0
tcount = 0
xcount = 0

while True:
    error = lscor.reflection() - rscor.reflection()
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
    # 1 VERDE
        # viu verde primeiro, sendo que está depois do preto **
        # viu verde primeiro, sendo que está antes do preto
    if (lscor.color() == Color.GREEN) != (rscor.color() == Color.GREEN):
        if lscor.color() == Color.GREEN:
            count += 1 
        elif rscor.color() == Color.GREEN:
            count += 1 
        else:
            count = 0
    else:
        count = 0

    if count == 3:
        if lscor.color() == Color.GREEN:
                robot.straight(30)
                gyro_90neg()
        elif rscor.color() == Color.GREEN:
                robot.straight(30)
                gyro_90()
                count = 0

        # beco sem saída
    if lscor.color() == Color.GREEN and rscor.color() == Color.GREEN:
        bcount += 1 
    else: 
        bcount = 0
    
    if bcount == 3:
        gyro_180()
        robot.straight(20)
    else:
        bcount = 0

        
    # INTERSEÇÃO onde não tem marcador verde
        # INTERSEÇÃO T 
    if (lscor.color() == Color.BLACK) and (rscor.color() == Color.WHITE):
        tcount += 1
    else:
        tcount = 0

    if (rscor.color() == Color.BLACK) and (lscor.color() == Color.WHITE):
        tcount += 1
    else:
        tcount = 0

    if tcount == 3:
        if (rscor.color() == Color.BLACK) and (lscor.color() == Color.WHITE):
            while lscor.color != Color.BLACK: 
                mgyro_10()
            tcount = 0

        elif (lscor.color() == Color.BLACK) and (rscor.color() == Color.WHITE):
            while rscor.color != Color.BLACK: 
                mgyro_10neg()
            tcount = 0

        else: 
            tcount = 0
    else:
        pass


        # INTERSEÇÃO X
    if (lscor.color() == Color.BLACK) and (rscor.color() == Color.BLACK):
        xcount += 1
    else:
        xcount = 0
    
    if xcount == 3:
        robot.straight(30)
    else:
        pass


    if ultras.distance() <= 40:
        robot.straight(-20)
        gyro_90()
        robot.straight(80)
        gyro_90neg()
        robot.straight(200)
        gyro_90neg()
        robot.straight(80)
        gyro_90()
        robot.straight(-50)



