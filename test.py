# import sys
# import time
# import atexit
# from constants import *
# from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
# from adafruit_motorkit import MotorKit
# from adafruit_motor import stepper

# create a default object, no changes to I2C address or frequency
# mh = Adafruit_MotorHAT(addr=0x70,freq=60)

# def turnOffMotors():
#     mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
#     mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
#     mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
#     mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

# atexit.register(turnOffMotors)

# myStepper = mh.getStepper(200, 1)
# myStepper.setSpeed(30)

# print("Single coil steps")
# myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
# myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

# print("Double coil steps")
# myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
# myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

# print("Interleaved coil steps")
# myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
# myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

# print("Microsteps")
# myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
# myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)

# atexit.register(turnOffMotors)

# kit = MotorKit()


# if sys.argv[1] == "--left":
#     for i in range(1000):
#         print(i)
#         kit.stepper1.onestep()
#         time.sleep(0.01)

# if sys.argv[1] == "--right":
#     for i in range(1000):
#         print(i)
#         kit.stepper1.onestep(direction=2)
#         time.sleep(0.01)

# if sys.argv[1] == "--up":
#     for i in range(1000):
#         print(i)
#         kit.stepper2.onestep()
#         time.sleep(0.01)

# if sys.argv[1] == "--down":
#     for i in range(1000):
#         print(i)
#         kit.stepper2.onestep(direction=2)
#         time.sleep(0.01)

# kit.stepper1.release()
# kit.stepper2.release()


#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()
st2 = threading.Thread()


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper1 = mh.getStepper(200, 1)      # 200 steps/rev, motor port #1
myStepper2 = mh.getStepper(200, 2)      # 200 steps/rev, motor port #1
myStepper1.setSpeed(60)          # 30 RPM
myStepper2.setSpeed(60)          # 30 RPM


stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
    stepper.step(numsteps, direction, style)
    #print("Done")

while (True):
    if not st1.isAlive():
        randomdir = random.randint(0, 1)
        print("Stepper 1"),
        if (randomdir == 0):
            dir = Adafruit_MotorHAT.FORWARD
            print("forward"),
        else:
            dir = Adafruit_MotorHAT.BACKWARD
            print("backward"),
        randomsteps = random.randint(10,50)
        print("%d steps" % randomsteps)
        st1 = threading.Thread(target=stepper_worker, args=(myStepper1, randomsteps, dir, stepstyles[random.randint(0,3)],))
        st1.start()

    if not st2.isAlive():
        print("Stepper 2"),
        randomdir = random.randint(0, 1)
        if (randomdir == 0):
            dir = Adafruit_MotorHAT.FORWARD
            print("forward"),
        else:
            dir = Adafruit_MotorHAT.BACKWARD
            print("backward"),

        randomsteps = random.randint(10,50)
        print("%d steps" % randomsteps)

        st2 = threading.Thread(target=stepper_worker, args=(myStepper2, randomsteps, dir, stepstyles[random.randint(0,3)],))
        st2.start()
    
    time.sleep(0.1)  # Small delay to stop from constantly polling threads (see: https://forums.adafruit.com/viewtopic.php?f=50&t=104354&p=562733#p562733)