import threading
import sys
import time
from constants import *
from step_controller import StepController


step_controller = StepController()
motor_thread = threading.Thread(target=step_controller.move)
motor_thread.start()

if sys.argv[1] == "--left":
    step_controller.set_directions(LEFT, IDLE)
    time.sleep(2)

elif sys.argv[1] == "--right":
    step_controller.set_directions(RIGHT, IDLE)
    time.sleep(2)

step_controller.set_run_flag(False)