import time
from adafruit_motorkit import MotorKit
import board

i2c = board.I2C()
# kit = MotorKit(i2c = i2c)

adresses = i2c.scan()
print("Bulunan cihazlar:")
for adress in adresses:
    print("adresses",hex(adress))

# import sys
# import time
# import atexit
# from constants import *
# from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
# from adafruit_motorkit import MotorKit

# # create a default object, no changes to I2C address or frequency
# # mh = Adafruit_MotorHAT(addr=112,freq=60)

# # def turnOffMotors():
# #     mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
# #     mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
# #     mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
# #     mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

# # atexit.register(turnOffMotors)

# # myStepper = mh.getStepper(200, 1)
# # myStepper.setSpeed(30)

# # while (True):
# #     print("Single coil steps")
# #     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
# #     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

# #     print("Double coil steps")
# #     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
# #     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

# #     print("Interleaved coil steps")
# #     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
# #     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

# #     print("Microsteps")
# #     myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
# #     myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)

# if sys.argv[1] == "--left":
#     for i in range(2000):
#         print(i)
#         kit.stepper1.onestep(direction=stepper.FORWARD, style=Mo.MICROSTEP)
#         time.sleep(0.005)

# if sys.argv[1] == "--right":
#     for i in range(2000):
#         print(i)
#         kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
#         time.sleep(0.005)

# if sys.argv[1] == "--up":
#     for i in range(2000):
#         print(i)
#         kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
#         time.sleep(0.005)

# if sys.argv[1] == "--down":
#     for i in range(2000):
#         print(i)
#         kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
#         time.sleep(0.005)

# kit.stepper1.release()
# kit.stepper2.release()