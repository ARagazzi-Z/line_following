from imports import *
ev3 = EV3Brick()

wd = wheel_diameter= 4
at = axle_track= 5
lm = Motor(Port.B)
rm = Motor(Port.C)
robot = DriveBase(lm, rm, wd, at)
sm = Motor(Port.D)
gm = Motor(Port.A)

gyro = GyroSensor(Port.S1)
ultras = UltrasonicSensor(Port.S2)
lscor = ColorSensor(Port.S3)
rscor = ColorSensor(Port.S4)

#CALIBRATION OF THE GYRO TO PREVENT DYNAMIC DRIFT
#Change from speed() (deg/sec) to angle() (deg) or from angle to speed.
def dynam_gauge():
    gyro.reset_angle(0)
    gyro.speed()
    wait(1000)
    gyro.angle()
    wait(1000)
    gyro.reset_angle(0)

#CALIBRATION OF THE GYRO TO PREVENT STATIC DRIFT
#Calculates the difference between the reference(that the robot should have gone) and the drift (the wrong drift)
ref = 0 # the robot should have gone at that moment
def static_gauge():
    drift = ref - gyro.angle()

#CALIBRAR COM ELE TOTALMENTE PARADO 

#SEMPRE CALIBRAR O GYRO AO BATER EM UMA PAREDE PARA EVITAR O *DRIFT ESTÁTICO*
#A CALIBRAÇÃO DO DRIFT DINÂMICO PODE SER FEITO AO INÍCIO DO ROUND

def scor_reflection_data():
    x = lscor.reflection()
    y = rscor.reflection()

    ev3.screen.print('esquerda:')(x)
    ev3.screen.print('direita:')(y)

# Escreve na tela a quantidade de luz refletida que cada sensor está vendo