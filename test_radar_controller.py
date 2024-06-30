import math
import time
import gpiozero
import numpy as np
import threading
import keyboard
from utils.constants import *
from controllers.lidar_controller import LidarController
from controllers.step_controller import StepController

lidar_array = []
lidar_controller = LidarController()

lidar_stepper = StepController(DIR_PIN_HOR, STEP_PIN_HOR)
lidar_stepper.set_directions(FORWARD)

turret_stepper = StepController(DIR_TURRET_LR, STEP_TURRET_LR)

motor_angle = MOTOR_HAT_ANGLES["4"]
step = LIDAR_SCAN_ANGLE / motor_angle
last_turret_angle = 0
counter = round(step / 2)
direction = True

def calculate_turret_alpha_degree(x_distance:int, beta_angle:int):
    z_angle =  180 - (LIDAR_SCAN_ANGLE / 2) + beta_angle
    z_square = (x_distance ** 2) + (LIDAR_STEPPER_DISTANCE ** 2) - (2*LIDAR_STEPPER_DISTANCE*x_distance*math.cos(math.radians(z_angle)))
    sin_g = (math.sin(math.radians(z_angle)) / math.sqrt(z_square)) * x_distance
    g_value_radient = math.asin(sin_g)
    g_value_degree = math.degrees(g_value_radient)
    return g_value_degree

def turret_stepper_move(angle):
    counter = 0
    step = angle / motor_angle
    step = step * 5
    while counter < step:
        turret_stepper.move_by_direction(0.001)
        counter += 1

if __name__ == "__main__":
    try:
        if lidar_controller.is_open() == False:
            lidar_controller.open()
        while True:
            if counter >= step:
                if direction == True:
                    lidar_stepper.set_directions(BACKWARD)
                    lidar_array.reverse() ## if direction == BACKWARD then reverse array
                    direction = False
                elif direction == False:
                    lidar_stepper.set_directions(FORWARD)
                    direction = True
                counter = 0
                left_index,right_index, mid_index = lidar_controller.find_object_angles(lidar_array)
                if left_index is not None:
                    # print(f"Object is between {(left_index * motor_angle):.2f} and {(right_index * motor_angle):.2f} angles")
                    print(f"Object angle is {(mid_index * motor_angle):.2f}")
                    print(f"Object mid point distance is {float(lidar_array[mid_index]):.2f}")
                    turret_angle = calculate_turret_alpha_degree(float(lidar_array[mid_index]),mid_index*motor_angle)
                    print(f"Turret angle : ",turret_angle)
                    lidar_array.clear()
                    if last_turret_angle == -(turret_angle):
                        diff = last_turret_angle + turret_angle
                    else:
                        diff = last_turret_angle - turret_angle
                    last_turret_angle = turret_angle
                    if diff < 0:
                        turret_stepper.set_directions(BACKWARD)
                    elif diff > 0:
                        turret_stepper.set_directions(FORWARD)
                    turret_thread = threading.Thread(target=turret_stepper_move(abs(diff)))
                    turret_thread.start()
                    turret_thread.join()
                else: 
                    print(f"No object Found")
                    lidar_array.clear()
            lidar_stepper.move_by_direction(LIDAR_SCANNER_DURATION)
            counter = counter + 1
            
            lidar_controller.run_lidar()
            lidar_array.append(lidar_controller.get_distance())


    except KeyboardInterrupt(): # ctrl + c in terminal.
        if lidar_controller.get_ser() != None:
            lidar_controller.close()
        
        ls_reset_step = step - counter
        lidar_stepper.set_directions(not direction)
        lidar_stepper.move_by_step(ls_reset_step)
        
        ts_direction = diff < 0
        turret_stepper.set_directions(not ts_direction)
        lidar_stepper.move_by_step(abs(diff))
