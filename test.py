import time
from utils.constants import *
from controllers.lidar_controller import LidarController

lidar_controller = LidarController()

while True:
    lidar_controller.trigger()
    lidar_controller.calculate_pulse_duration()
    distance = lidar_controller.get_distance_cm()
    print(f"Distance: {distance} cm")
    sleep_time = 1 / 10
    time.sleep(sleep_time)