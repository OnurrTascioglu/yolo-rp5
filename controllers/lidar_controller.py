import time
import serial
from utils.constants import *


class LidarController:
    distance = 0
    temperature = 0
    strength = 0
    
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0", 115200)
        time.sleep(0.1)

    def is_open(self):
        return self.ser.isOpen()
        
    def open(self):
        self.ser.open()
    
    def close(self):
        self.ser.close()
    
    def get_ser(self):
        return self.ser

    def run_lidar(self):
        counter = self.ser.in_waiting 
        if counter > 8:
            bytes_serial = self.ser.read(9)
            self.ser.reset_input_buffer()
            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:      
                self.distance = bytes_serial[2] + bytes_serial[3]*256 # multiplied by 256, because the binary data is shifted by 8 to the left (equivalent to "<< 8").                                              # Dist_L, could simply be added resulting in 16-bit data of Dist_Total.
                self.strength = bytes_serial[4] + bytes_serial[5]*256
                self.temperature = bytes_serial[6] + bytes_serial[7]*256
                self.temperature = (self.temperature/8) - 256
                self.ser.reset_input_buffer()

    def get_distance(self):
        return str(self.distance)
    
    def get_strenght(self):
        return str(self.strength)
        
    def get_temperature(self):
        return str(self.temperature)
