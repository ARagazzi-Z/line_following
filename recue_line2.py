from functions import *
from imports import * 
from gyro_move import gyro_straight
from gyro_turn import gyro_90, gyro_90neg, gyro_180, gyro_10neg, gyro_10

back = 0 # distancia que o robo percorreu desde de a entrada da área de resgate até os 3 seg. *CALCULAR*

if (lscor.color() == Color.WHITE) and (rscor.color() == Color.WHITE):
    wait(3000)
    if (lscor.color() == Color.WHITE) and (rscor.color() == Color.WHITE):
        while True: 
            gcount1 = 0 
            if ultras.distance() + back <= 1200: # verifica se NÃO é a saída
                point1 = ultras.distance() + back
                if point1 <= 1000: # se for a medida de 120 na entrada
                    robot.straight(60-back)
                    gyro_90neg() # gira para a esquerda
                    if ultras.distance() <= 30: # se a entrada for no canto da esquerda
                        robot.straight(-20)
                        gyro_180()
                        robot.straight(450)
                        if ultras.distance() > 750:
                            sm.run_target(360, 100) # ativação do sensor de cor para resgate
                            while ultras.distance() >= 300:
                                gyro_10()
                                gcount1 += 1
                                wait(100)
                                if gcount1 >= 36: 
                                    break 
                            if gcount1 < 36:
                                ball1 = ultras.distance()
                                robot.straight(ball1 - 20)
                                gyro_10neg() # para que o sensor de cor veja
                                if rscor.color() == Color.BLACK:
                                    robot.straight(-30)
                                    gyro_180() 
                                    gm.run_target(200, 30)
                                    robot.straight(-70)
                                    gm.run_target(200, -30)
                                elif rscor.color() == Color.WHITE:
                                    robot.straight(-30)
                                    gyro_180() 
                                    gm.run_target(200, -30)
                                    robot.turn(20)
                                    robot.straight(-70)
                                    gm.run_target(200, -30)

                            elif gcount1 >= 36:
                                robot.straight(30)
                                gcount2 = 0
                                while ultras.distance() >= 300:
                                    gyro_10()
                                    gcount2 += 1
                                    wait(100)
                                    if gcount2 >= 36: 
                                        break 
                                if gcount1 < 36:
                                    ball1 = ultras.distance()
                                    robot.straight(ball1 - 20)
                                    gyro_10neg() # para que o sensor de cor veja    
                                    if rscor.color() == Color.BLACK:
                                        robot.straight(-30)
                                        gyro_180() 
                                        gm.run_target(200, 30)
                                        robot.straight(-70)
                                        gm.run_target(200, -30)
                                    elif rscor.color() == Color.WHITE:
                                        robot.straight(-30)
                                        gyro_180() 
                                        gm.run_target(200, -30)
                                        robot.turn(20)
                                        robot.straight(-70)
                                        gm.run_target(200, -30)
                                elif gcount2 >= 36:
                                    gyro_180()
                                    robot.straight(60)
                                    gcount3 = 0
                                    while ultras.distance() >= 300:
                                        gyro_10()
                                        gcount2 += 1
                                        wait(100)
                                        if gcount2 >= 36: 
                                            break 
                                    if gcount1 < 36:
                                        ball1 = ultras.distance()
                                        robot.straight(ball1 - 20)
                                        gyro_10neg() # para que o sensor de cor veja    
                                        if rscor.color() == Color.BLACK:
                                            robot.straight(-30)
                                            gyro_180() 
                                            gm.run_target(200, 30)
                                            robot.straight(-70)
                                            gm.run_target(200, -30)
                                        elif rscor.color() == Color.WHITE:
                                            robot.straight(-30)
                                            gyro_180() 
                                            gm.run_target(200, -30)
                                            robot.turn(20)
                                            robot.straight(-70)
                                            gm.run_target(200, -30)


                elif 850 <= point1 < 950: # o 85 é para se tiver uma vitima na frente até 85 cm. O escesso é para margem de erro.
                        front = point1 / 2 
                        robot.straight(front)
                        gyro_90neg() # gira para a esquerda
                        if ultras.distance() <= 30: # se a entrada for no canto da esquerda
                            robot.straight(-20)
                            gyro_180()
                            if ultras.distance() > 750:
                                middle = ultras.distance() / 2 
                                robot.straight(middle) # ir até o centro
                                sm.run_target(360, 100) # ativação do sensor de cor para resgate
                                while ultras.distance() >= 300:
                                    robot.turn(-10)
                                    wait(100)
                                ball1 = ultras.distance()
                                robot.straight(ball1 - 20)
                                gyro_10neg # para que o sensor de cor veja
                else: 
                        ball1 = ultras.distance()
                        robot.straight(ball1 - 30)
                    
