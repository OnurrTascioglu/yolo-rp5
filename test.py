import threading
import sys
import time
from constants import *
from adafruit_motor import stepper
from step_controller import StepController
from adafruit_motorkit import MotorKit
import board

kit = MotorKit(i2c=board.I2C())

if sys.argv[1] == "--left":
    for i in range(1):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)

if sys.argv[1] == "--right":
    for i in range(1):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

if sys.argv[1] == "--up":
    for i in range(1):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)

if sys.argv[1] == "--down":
    for i in range(1):
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

kit.stepper1.release()
kit.stepper2.release()