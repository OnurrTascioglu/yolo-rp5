import time
import gpiozero
from utils.constants import *


class LidarController:
    pulse_duration = 0
    pulse_start = 0
    current_state = None
    
    def __init__(self):
        self.trigger_pin = gpiozero.OutputDevice(TRIGGER_PIN)
        self.echo_pin = gpiozero.InputDevice(ECHO_PIN)

    def trigger(self):
        self.trigger_pin.on()
        time.sleep(TRIGGER_TIME)
        self.trigger_pin.off()

    def echo_pin_test(self):
        print(self.echo_pin.value)
        while True:
            if self.echo_pin.value == self.current_state:
                continue
            else:
                print(self.current_state, self.echo_pin.value)
                self.current_state = self.echo_pin.value

    def calculate_pulse_duration(self):
        while self.echo_pin.value == 1:
            pulse_end = time.time()
            # print("End_time :", pulse_end)
        self.pulse_duration = pulse_end - self.pulse_start
    
    def get_distance_cm(self):
        print("pulse duration:", self.pulse_duration)
        ## 17241.379310344827586206896551724
        distance = 300000 / self.pulse_duration
        return distance

    def cleanup(self):
        self.trigger_pin.close()
        self.echo_pin.close()
