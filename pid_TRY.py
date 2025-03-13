from functions import *
from imports import *
from gyro_turn import gyro_90

"""
     P (Proporcional): Multiplica o erro por kp para corrigir a direção.
     I (Integral): Acumula pequenos erros ao longo do tempo.
     D (Derivada): Reage a mudanças rápidas no erro para evitar oscilações.
"""
# PID - color sensor
kp = 3
ki = 0
kd = 6.5

last_error = 0
integral = 0
count = 0
speed = 30 

while True:
    error = lscor.reflection() - rscor.reflection()
    P = error * kp
    integral += error
    I = integral * ki
    D = (error - last_error)* kd
    line_turn = P + I + D 

    last_error = error #atualiza o erro


# PID - gyro move
    gkp = -1.7
    gki = 0
    gkd = -10

    gintegral = 0
    glast_error = 0

    ref = 0 # andar reto

    # ref é a referência, o valor que quer chegar
    # A EQUAÇÃO: Erro = [leitura do sensor] - [ref] 

    gerror = gyro.angle() - ref
    Pg = gerror * gkp
    gintegral += gerror
    Ig = integral * gki
    Dg = (gerror - glast_error)* gkd
    gyro_turn = Pg + Ig + Dg 
           
    glast_error = gerror #atualiza o erro

# TURN VALUE
    turn = gyro_turn + line_turn
    robot.drive(speed, turn)

    wait(10)

# LEITURA DO VERDE
    # 1 VERDE
        # viu verde primeiro, sendo que está depois do preto
        # viu verde primeiro, sendo que está antes do preto
    if (lscor.color() == Color.GREEN) != (rscor.color() == Color.GREEN):
        robot.straight(-35)
        if lscor.color() == Color.BLACK or rscor.color() == Color.BLACK:
            count = 0
            robot.straight(45)
        else:
            count += 1
    else:
        count = 0

    if count == 3:
        if lscor.color() == Color.GREEN:
                robot.turn(20, -90)
                count = 0
        elif rscor.color() == Color.GREEN:
                robot.turn(20, 90)
                count = 0

        # beco sem saída
    if lscor.color() == Color.GREEN and rscor.color() == Color.GREEN:
        robot.turn(20, 180)
    else: 
        pass
        
    # INTERSEÇÃO onde não tem marcador verde
        # INTERSEÇÃO T 
    if (lscor.color() == Color.BLACK) != (rscor.color() == Color.BLACK):
        if lscor.color() == Color.BLACK: 
            while rscor.color != Color.BLACK:
                robot.drive(20, -10)      
        elif rscor.color() == Color.BLACK: 
            while lscor.color != Color.BLACK:
                robot.drive(20, 10)

        # INTERSEÇÃO +
    if (lscor.color() == Color.BLACK) and (rscor.color() == Color.BLACK):
        robot.straight(30)





