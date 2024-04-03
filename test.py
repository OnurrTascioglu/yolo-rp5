import threading
import sys
import time
from constants import *
from adafruit_motor import stepper
from step_controller import StepController
from adafruit_motorkit import MotorKit
import board

kit = MotorKit(i2c=board.I2C())
kit.frequency = 1600

if sys.argv[1] == "--left":
    for i in range(2000):
        print(i)
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        time.sleep(0.005)

if sys.argv[1] == "--right":
    for i in range(2000):
        print(i)
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        time.sleep(0.005)

if sys.argv[1] == "--up":
    for i in range(2000):
        print(i)
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        time.sleep(0.005)

if sys.argv[1] == "--down":
    for i in range(2000):
        print(i)
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        time.sleep(0.005)

kit.stepper1.release()
kit.stepper2.release()