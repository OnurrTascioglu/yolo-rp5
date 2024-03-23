import time
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
from constants import *


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
    run_flag = False

    def __init__(self) -> None:
        self.kit = MotorKit(i2c=board.I2C())
        self.run_flag = True

    def move_left(self, step):
        print("Moving left")
        self.kit.stepper1.onestep(direction=stepper.FORWARD, style=step)
        time.sleep(0.01)
    
    def move_right(self, step):
        print("Moving right")
        self.kit.stepper1.onestep(direction=stepper.BACKWARD, style=step)
        time.sleep(0.01)
    
    def move_up(self, step):
        print("Moving up")
        self.kit.stepper2.onestep(direction=stepper.FORWARD, style=step)
        time.sleep(0.01)
    
    def move_down(self, step):
        print("Moving down")
        self.kit.stepper2.onestep(direction=stepper.BACKWARD, style=step)
        time.sleep(0.01)

    def release_horizontal(self):
        print("Releasing horizontal")
        self.kit.stepper1.release()
    
    def release_vertical(self):
        print("Releasing vertical")
        self.kit.stepper2.release()

    def release(self):
        self.kit.stepper1.release()
        self.kit.stepper2.release()
    
    def set_directions(self, direction_x, direction_y):
        self.current_direction_horizontal = direction_x
        self.current_direction_vertical = direction_y
    
    def set_run_flag(self, flag):
        self.run_flag = flag
    
    def move(self):
        while self.run_flag:
            if self.current_direction_horizontal == LEFT:
                self.move_left(step=stepper.SINGLE)
            elif self.current_direction_horizontal == RIGHT:
                self.move_right(step=stepper.SINGLE)
            elif self.current_direction_horizontal == IDLE:
                self.release_horizontal()
        
            if  self.current_direction_vertical == UP:
                self.move_up(step=stepper.SINGLE)
            elif  self.current_direction_vertical == DOWN:
                self.move_down(step=stepper.SINGLE)
            elif  self.current_direction_vertical == IDLE:
                self.release_vertical()
            time.sleep(0.01)

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
        if abs(mid_x - CENTER_X) > TARGET_LOCK_THRESHOLD_PIXELS:
            if mid_x < CENTER_X:
                horizontal = LEFT
            elif mid_x > CENTER_X:
                horizontal = RIGHT

        if abs(mid_y - CENTER_Y) > TARGET_LOCK_THRESHOLD_PIXELS:
            if mid_y < CENTER_Y:
                vertical = UP
            elif mid_y > CENTER_Y:
                vertical = DOWN
        return horizontal, vertical