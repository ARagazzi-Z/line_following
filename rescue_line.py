from functions import *
from imports import *
from gyro_turn import gyro_90, gyro_180, gyro_90neg, gyro_10neg, gyro_10
from gyro_move import gyro_straight


back = 0 # distancia que o robo percorreu desde de a entrada da área de resgate até os 3 seg. CALCULAR

if (lscor.color() == Color.WHITE) and (rscor.color() == Color.WHITE):
    wait(3000)
    if (lscor.color() == Color.WHITE) and (rscor.color() == Color.WHITE):
        if ultras.distance() <= 1200: # verifica se é a saída
            point1 = ultras.distance() + back
            if 300 <= point1 <= 900:
                front = point1 / 2 
                robot.straight(front)
                gyro_90neg() # gira para a esquerda
            elif point1 >= 910:
                pass # FAZER

            if ultras.distance() <= 30: # se a entrada for no canto da esquerda
                robot.straight(-20)
                gyro_180()
                if ultras.distance() >= 750:
                    middle = ultras.distance() / 2 
                    robot.straight(middle) # ir até o centro
                    sm.run_target(360, 100) # ativação do sensor de cor para resgate
                    while ultras.distance() >= 300:
                        robot.turn(-10)
                        wait(100)
                    ball1 = ultras.distance()
                    robot.straight(ball1 - 20)
                    gyro_10neg # para que o sensor de cor veja
                    if rscor.color() == Color.WHITE:
                        # RESGATE VITIMAS VIVAS
                        robot.straight(-150) # se afastou da vitima
                        gm.run_target(40, 80) # desceu a pá
                        gyro_180 # a pá em direção à vítima
                        robot.straight(-200)
                        robot.drive(0,0)
                        lm.brake()
                        rm.brake()
                        gm.run_target(20, 30)
                        gm.run_target(20, -30)
                    elif rscor.color() == Color.BLACK:
                        # RESGATE VITIMAS MORTAS
                        gyro_10() # girar para alinhar a vitima ao espaço das mortas na pá
                        robot.straight(-150) # se afastou da vitima
                        gm.run_target(40, 80) # desceu a pá
                        gyro_180 # a pá em direção à vítima
                        robot.straight(-200)
                        gm.run_target(20, 30)
                        gm.run_target(20, -30)


            elif ultras.distance() <= 750:
                sm.run_target(360, 100) # ativação do sensor de cor para resgate
                ball1 = ultras.distance()
                robot.straight(ball1 - 20)
                gyro_10neg # para que o sensor de cor veja
                if rscor.color() == Color.WHITE:
                    # RESGATE VITIMAS VIVAS
                    robot.straight(-150) # se afastou da vitima
                    gm.run_target(40, 80) # desceu a pá
                    gyro_180 # a pá em direção à vítima
                    robot.straight(-200)
                    robot.drive(0,0)
                    lm.brake()
                    rm.brake()
                    gm.run_target(20, 30)
                    gm.run_target(20, -30)
                elif rscor.color() == Color.BLACK:
                    # RESGATE VITIMAS MORTAS
                    gyro_10() # girar para alinhar a vitima ao espaço das mortas na pá
                    robot.straight(-150) # se afastou da vitima
                    gm.run_target(40, 80) # desceu a pá
                    gyro_180 # a pá em direção à vítima
                    robot.straight(-200)
                    gm.run_target(20, 30)
                    gm.run_target(20, -30)

        elif ultras.distance() >= 750:
            middle = ultras.distance() / 2 
            robot.straight(middle)
            sm.run_target()
            while ultras.distance() <= 300:
                robot.turn(-10)

        else: 
            if ultras.distance() >= 750:
                middle = ultras.distance() / 2
                robot.straight(middle)




