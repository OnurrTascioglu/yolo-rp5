#import time
#from utils.constants import *
#from controllers.lidar_controller import LidarController

#lidar_controller = LidarController()


#while True:
    #lidar_controller.trigger()
    #lidar_controller.echo_pin_test()
    #lidar_controller.trigger()
    #lidar_controller.calculate_pulse_duration()
    #distance = lidar_controller.get_distance_cm()
    #print(f"Distance: {distance} cm")
    #sleep_time = 2
    #time.sleep(sleep_time)


# -*- coding: utf-8 -*
import time
import serial
# written by Ibrahim for Public use

# Checked with TFmini plus

# ser = serial.Serial("/dev/ttyUSB1", 115200)

ser = serial.Serial("/dev/ttyAMA0", 115200)
# ser = serial.Serial("COM12", 115200)


# we define a new function that will get the data from LiDAR and publish it
def read_data():
    counter_2 = 0
    while True:
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = ser.read(9)
            ser.reset_input_buffer()

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # this portion is for python3
                print("Printing python3 portion")            
                distance = bytes_serial[2] + bytes_serial[3]*256 # multiplied by 256, because the binary data is shifted by 8 to the left (equivalent to "<< 8").                                              # Dist_L, could simply be added resulting in 16-bit data of Dist_Total.
                strength = bytes_serial[4] + bytes_serial[5]*256
                temperature = bytes_serial[6] + bytes_serial[7]*256
                temperature = (temperature/8) - 256
                print("Distance:"+ str(distance))
                print(counter_2)
                counter_2 = counter_2 + 1
                #print("Strength:" + str(strength))
                #if temperature != 0:
                #    print("Temperature:" + str(temperature))
                ser.reset_input_buffer()
        

if __name__ == "__main__":
    try:
        if ser.isOpen() == False:
            ser.open()
        read_data()
    except KeyboardInterrupt(): # ctrl + c in terminal.
        if ser != None:
            ser.close()
            print("program interrupted by the user")
