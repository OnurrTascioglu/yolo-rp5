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
    current_direction = IDLE
    direction_pin = None
    step_pin = None
    step_wait_time = 0.001 ## default == 0.0075
    run_flag = False

    def __init__(self, direction_pin:int, step_pin:int) -> None:
        self.run_flag = True
        self.direction_pin = gpiozero.OutputDevice(direction_pin)
        self.step_pin = gpiozero.OutputDevice(step_pin)

    def move_forward(self):
        self.direction_pin.on()
        self.step_pin.on()
        time.sleep(self.step_wait_time)
        self.step_pin.off()
        time.sleep(self.step_wait_time)
    
    def move_backward(self):
        self.direction_pin.off()
        self.step_pin.on()
        time.sleep(self.step_wait_time)
        self.step_pin.off()
        time.sleep(self.step_wait_time)

    def release(self):
        self.step_pin.off()
    
    def set_directions(self, direction):
        self.current_direction = direction
    
    def set_speed(self, time):
        self.step_wait_time = time
    
    def set_run_flag(self, flag):
        self.run_flag = flag
    
    def move_by_direction(self, sleep_time=0.025):
        if self.run_flag:
            if self.current_direction == BACKWARD:
                self.move_backward()
            elif self.current_direction == FORWARD:
                self.move_forward()
            elif self.current_direction == IDLE:
                self.release()
            time.sleep(sleep_time)
    
    def move_by_step(self, step)
        for _ in range(0,step):
            if self.current_direction == BACKWARD:
                self.move_backward()
            elif self.current_direction == FORWARD:
                self.move_forward()
            elif self.current_direction == IDLE:
                self.release()
            time.sleep(sleep_time)


    @staticmethod
    def get_turret_next_directions(mid_x, mid_y):
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
