import time
from controllers.lidar_controller import LidarController

lidar_controller = LidarController()

if __name__ == "__main__":
    try:
        if lidar_controller.is_open() == False:
            lidar_controller.open()
        while True:
            lidar_controller.run_lidar()
            print(lidar_controller.get_distance())
            time.sleep(1)
    except KeyboardInterrupt(): # ctrl + c in terminal.
        if lidar_controller.get_ser() != None:
            lidar_controller.close()
