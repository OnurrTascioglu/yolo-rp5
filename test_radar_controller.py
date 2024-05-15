import time
import gpiozero
import numpy as np
from utils.constants import *
from controllers.lidar_controller import LidarController
from controllers.step_controller import StepController

lidar_array = []
lidar_controller = LidarController()

lidar_stepper = StepController(DIR_PIN_HOR, STEP_PIN_HOR)

motor_angle = MOTOR_HAT_ANGLES["4"]
step = LIDAR_SCAN_ANGLE // motor_angle
counter = 0
direction = True

if __name__ == "__main__":
    try:
        if lidar_controller.is_open() == False:
            lidar_controller.open()
        while True:
            if counter == step:
                if direction == True:
                    lidar_stepper.set_directions(BACKWARD)
                    lidar_array.reverse() ## if direction == BACKWARD then reverse array
                    direction = False
                elif direction == False:
                    lidar_stepper.set_directions(FORWARD)
                    direction = True
                counter = 0
                left_index,right_index, mid_index = lidar_controller.find_object_angles(lidar_array)
                print(f"Object is between {(left_index * motor_angle):.2f} and {(right_index * motor_angle):.2f} angles")
                print(f"Object mid point distance is {lidar_array[mid_index]:.2f}")
                lidar_array.clear()
            lidar_stepper.move_by_direction(LIDAR_SCANNER_DURATION)
            counter = counter + 1
            
            lidar_controller.run_lidar()
            lidar_array.append(lidar_controller.get_distance())

    except KeyboardInterrupt(): # ctrl + c in terminal.
        if lidar_controller.get_ser() != None:
            lidar_controller.close()
