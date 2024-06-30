import math
import threading
import keyboard
from utils.helpers import *
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
lidar_stepper.set_direction(BACKWARD)

running = True
def on_key_event(e:keyboard.KeyboardEvent):
    if e.name == 'q':
        print("Exiting")
        global running
        running = False

if __name__ == "__main__":
    try:
        keyboard.hook_key('q', on_key_event)
        if lidar_controller.is_open() == False:
            lidar_controller.open()
        while True:
            if counter >= step:
                lidar_stepper.change_direction()
                if lidar_stepper.get_direction() == BACKWARD:
                    lidar_array.reverse() ## if direction == BACKWARD then reverse array
                counter = 0
                left_index,right_index, mid_index = lidar_controller.find_object_angles(lidar_array)
                if left_index is not None:
                    print(f"Object angle is {(mid_index * motor_angle):.2f}")
                    print(f"Object mid point distance is {float(lidar_array[mid_index]):.2f}")
                    turret_angle = calculate_turret_alpha_degree(float(lidar_array[mid_index]),mid_index*motor_angle)
                    
                    lidar_array.clear()
                    angle_diff = calculate_turret_angel_difference(last_turret_angle, turret_angle)
                    
                    if angle_diff < 0:
                        turret_stepper.set_direction(BACKWARD)
                    elif angle_diff > 0:
                        turret_stepper.set_direction(FORWARD)
                        
                    last_turret_angle = turret_angle
                    turret_thread = threading.Thread(turret_stepper.turret_stepper_move(abs(angle_diff),motor_angle,5))
                    turret_thread.start()
                    turret_thread.join()
                else: 
                    print(f"No object Found")
                    lidar_array.clear()
            lidar_stepper.move_by_direction(LIDAR_SCANNER_DURATION)
            counter = counter + 1
            
            lidar_controller.run_lidar()
            lidar_array.append(lidar_controller.get_distance())

            if not running:
                ls_reset_step = step / 2
                lidar_stepper.change_direction()
                lidar_stepper.move_by_step(ls_reset_step)
                
                ts_direction = angle_diff < 0
                turret_stepper.set_direction(not ts_direction)
                lidar_stepper.move_by_step(abs(angle_diff))

    except KeyboardInterrupt(): # ctrl + c in terminal.
        if lidar_controller.get_ser() != None:
            lidar_controller.close()
