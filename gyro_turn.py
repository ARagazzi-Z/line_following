from functions import *
from imports import *


kp = -0.6
ki = -0.01
kd = -4
integral = 0
last_error = 0



# ref é a referência, o valor que quer chegar
# A EQUAÇÃO: Erro = [leitura do sensor] - [ref] 
def gyro_90():  
    while True:
        ref = 90 
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
        
        lturn = turn * 1
        rturn = turn * -1
        last_error = error #atualiza o erro

        ref = abs(ref) # tornando a referencia um numero absoluto 
        # tornando o angulo lido pelo gyro um numero absoluto
        # isso torna mais fácil a certificação.

        while not abs(gyro.angle())>= ref:
            robot.stop() # para permitir que os motores atuem separadamente
            lm.run(lturn)
            rm.run(rturn)
        robot.stop()
        lm.brake()
        rm.brake()

def gyro_180():  
    while True:
        ref = 180
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
            
        lturn = turn * 1
        rturn = turn * -1
        last_error = error #atualiza o erro

        ref = abs(ref) # tornando a referencia um numero absoluto 
        # tornando o angulo lido pelo gyro um numero absoluto
        # isso torna mais fácil a certificação.

        while not abs(gyro.angle())>= ref:
            robot.stop() # para permitir que os motores atuem separadamente
            lm.run(lturn)
            rm.run(rturn)
        robot.stop()
        lm.brake()
        rm.brake()

        
def gyro_90neg():  
    while True:
        ref = -90 
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
        
        lturn = turn * 1
        rturn = turn * -1
        last_error = error #atualiza o erro

        ref = abs(ref) # tornando a referencia um numero absoluto 
        # tornando o angulo lido pelo gyro um numero absoluto
        # isso torna mais fácil a certificação.

        while not abs(gyro.angle())>= ref:
            robot.stop() # para permitir que os motores atuem separadamente
            lm.run(lturn)
            rm.run(rturn)
        robot.stop()
        lm.brake()
        rm.brake()


def gyro_10neg():  
    while True:
        ref = -10
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
        
        lturn = turn * 1
        rturn = turn * -1
        last_error = error #atualiza o erro

        ref = abs(ref) # tornando a referencia um numero absoluto 
        # tornando o angulo lido pelo gyro um numero absoluto
        # isso torna mais fácil a certificação.

        while not abs(gyro.angle())>= ref:
            robot.stop() # para permitir que os motores atuem separadamente
            lm.run(lturn)
            rm.run(rturn)
        robot.stop()
        lm.brake()
        rm.brake()


def gyro_10():  
    while True:
        ref = 10
        error = gyro.angle() - ref
        P = error * kp
        integral += error
        I = integral * ki
        D = (error - last_error)* kd
        turn = P + I + D 
        
        lturn = turn * 1
        rturn = turn * -1
        last_error = error #atualiza o erro

        ref = abs(ref) # tornando a referencia um numero absoluto 
        # tornando o angulo lido pelo gyro um numero absoluto
        # isso torna mais fácil a certificação.

        while not abs(gyro.angle())>= ref:
            robot.stop() # para permitir que os motores atuem separadamente
            lm.run(lturn)
            rm.run(rturn)
        robot.stop()
        lm.brake()
        rm.brake()