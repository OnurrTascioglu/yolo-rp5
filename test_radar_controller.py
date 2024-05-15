import time
import gpiozero
import numpy as np
from utils.constants import *
from controllers.lidar_controller import LidarController
from controllers.step_controller import StepController

lidar_array = []
lidar_controller = LidarController()

direction_pin_horizontal = gpiozero.OutputDevice(DIR_PIN_HOR)
step_pin_horizontal = gpiozero.OutputDevice(STEP_PIN_HOR)

direction_pin_horizontal.on()

motor_angle = MOTOR_HAT_ANGLES["4"]
step = LIDAR_SCAN_ANGLE // motor_angle
counter = 0
direction = True

def find_object_angles(array:list):
    array = np.array(array).astype(np.int16)
    q1 = np.percentile(array, 25)

    small_indexes = np.where(array < q1)[0]  ## get indexes
    groups = np.split(small_indexes, np.where(np.diff(small_indexes) != 1)[0]+1)
    max_group = max(groups, key=len)
    mid_index = max_group[len(max_group)//2]
    
    return max_group[0], max_group[-1], mid_index


if __name__ == "__main__":
    try:
        if lidar_controller.is_open() == False:
            lidar_controller.open()
        while True:
            if counter == step:
                direction = StepController.change_direction(direction)
                if direction == True: ## if moving left reverse array
                    lidar_array.reverse()
                counter = 0
                left_index,right_index, mid_index = find_object_angles(lidar_array)
                left_angle = left_index * motor_angle
                right_angle = right_index * motor_angle
                mid_angle = mid_index * motor_angle
                print(f"Object is between {left_angle:.2f} and {right_angle:.2f} angles")
                print(f"Object mid point distance is {lidar_array[mid_index]:.2f}")
                lidar_array.clear()
            step_pin_horizontal.on()
            time.sleep(LIDAR_SCANNER_DURATION)
            step_pin_horizontal.off()
            time.sleep(LIDAR_SCANNER_DURATION)
            counter = counter + 1
            
            lidar_controller.run_lidar()
            lidar_array.append(lidar_controller.get_distance())

    except KeyboardInterrupt(): # ctrl + c in terminal.
        if lidar_controller.get_ser() != None:
            lidar_controller.close()
