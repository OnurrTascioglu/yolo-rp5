import time
import gpiozero
from utils.constants import *


class LidarController:
    pulse_duration = 0
    def __init__(self):
        self.trigger_pin = gpiozero.OutputDevice(TRIGGER_PIN)
        self.echo_pin = gpiozero.OutputDevice(ECHO_PIN)

    def trigger(self):
        self.trigger_pin.on()
        time.sleep(TRIGGER_TIME)
        self.trigger_pin.off()

    def calculate_pulse_duration(self):
        while self.echo_pin.is_active == False:
            pulse_start = time.time()
        while self.echo_pin.is_active == True:
            pulse_end = time.time()
        self.pulse_duration = pulse_end - pulse_start
    
    def get_distance_cm(self):
        distance = self.pulse_duration / DISTANCE_DIV_CONST
        return distance

    def cleanup(self):
        self.trigger_pin.close()
        self.echo_pin.close()