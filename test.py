import threading
import sys
import time
from constants import *
from adafruit_motor import stepper
from step_controller import StepController


step_controller = StepController()
# motor_thread = threading.Thread(target=step_controller.move)
# motor_thread.start()

if sys.argv[1] == "--left":
    for i in range(10):
        step_controller.move_left(stepper.DOUBLE)
        time.sleep(0.1)

if sys.argv[1] == "--right":
    for i in range(10):
        step_controller.move_right(stepper.DOUBLE)
        time.sleep(0.1)

step_controller.set_run_flag(False)
step_controller.release()