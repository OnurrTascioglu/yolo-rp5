import time
import gpiozero
from utils.constants import *

class StepController():
    """
    Class to control the stepper motors.

    Attributes:
        kit (MotorKit): Adafruit MotorKit object

    Note:
        Stepper1 = horizontal movements
        Stepper2 = vertical movements

        ## Motor informations
        -200 steps per revolution
        -15cm movement for 5m distance (1 step)
        -12cm movement for 4m distance (1 step)
        -
    """
    current_direction_horizontal = IDLE
    current_direction_vertical = IDLE
    direction_pin_horizontal = gpiozero.OutputDevice(DIR_PIN_HOR)
    direction_pin_vertical = gpiozero.OutputDevice(DIR_PIN_VER)
    step_pin_horizontal = gpiozero.OutputDevice(STEP_PIN_HOR)
    step_pin_vertical = gpiozero.OutputDevice(STEP_PIN_VER)
    step_wait_time = 0.001 ## default == 0.0075
    run_flag = False

    def __init__(self) -> None:
        self.run_flag = True

    def move_left(self):
        self.direction_pin_horizontal.on()
        self.step_pin_horizontal.on()
        time.sleep(self.step_wait_time)
        self.step_pin_horizontal.off()
        time.sleep(self.step_wait_time)
    
    def move_right(self):
        self.direction_pin_horizontal.off()
        self.step_pin_horizontal.on()
        time.sleep(self.step_wait_time)
        self.step_pin_horizontal.off()
        time.sleep(self.step_wait_time)
    
    def move_up(self):
        self.direction_pin_vertical.off()
        self.step_pin_vertical.on()
        time.sleep(self.step_wait_time)
        self.step_pin_vertical.off()
        time.sleep(self.step_wait_time)
    
    def move_down(self):
        self.direction_pin_vertical.on()
        self.step_pin_vertical.on()
        time.sleep(self.step_wait_time)
        self.step_pin_vertical.off()
        time.sleep(self.step_wait_time)

    def release_horizontal(self):
        self.step_pin_horizontal.off()
    
    def release_vertical(self):
        self.step_pin_vertical.off()

    def release(self):
        self.step_pin_horizontal.off()
        self.step_pin_vertical.off()
    
    def set_directions(self, direction_x, direction_y):
        print(f"Moving to {direction_x}, {direction_y}")
        self.current_direction_horizontal = direction_x
        self.current_direction_vertical = direction_y
    
    def set_speed(self, time):
        self.step_wait_time = time
    
    def set_run_flag(self, flag):
        self.run_flag = flag
    
    def move(self):
        while self.run_flag:
            if self.current_direction_horizontal == LEFT:
                self.move_left()
            elif self.current_direction_horizontal == RIGHT:
                self.move_right()
            elif self.current_direction_horizontal == IDLE:
                self.release_horizontal()
        
            if  self.current_direction_vertical == UP:
                self.move_up()
            elif  self.current_direction_vertical == DOWN:
                self.move_down()
            elif  self.current_direction_vertical == IDLE:
                self.release_vertical()
            time.sleep(0.025)

    @staticmethod
    def change_direction(direction):
        if direction == True:
            direction_pin_horizontal.off()
            print("Moving Right")
            direction = False
            return direction
        if direction == False:
            direction_pin_horizontal.on()
            print("Moving Left")
            direction = True
            return direction

    @staticmethod
    def get_stepper_next_directions(mid_x, mid_y):
        """
        Get the stepper motor direction based on the object's midpoint.
        
        Args:
            mid_x (int): x-coordinate of the object's midpoint
            mid_y (int): y-coordinate of the object's midpoint
        
        Returns:
            tuple: horizontal and vertical directions
        """
        horizontal = IDLE
        vertical = IDLE

        ## check if the object is within the target lock threshold
        if abs(mid_x - CENTER_X) > TARGET_LOCK_THRESHOLD_PIXELS_HORIZONTAL:
            if mid_x < CENTER_X:
                horizontal = LEFT
            elif mid_x > CENTER_X:
                horizontal = RIGHT

        if abs(mid_y - CENTER_Y) > TARGET_LOCK_THRESHOLD_PIXELS_VERTICAL:
            if mid_y < CENTER_Y:
                vertical = UP
            elif mid_y > CENTER_Y:
                vertical = DOWN
        return horizontal, vertical
