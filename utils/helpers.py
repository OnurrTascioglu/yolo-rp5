
import math
from utils.constants import *


def calculate_turret_alpha_degree(x_distance:int, beta_angle:int):
    z_angle =  180 - (LIDAR_SCAN_ANGLE / 2) + beta_angle
    z_square = (x_distance ** 2) + (LIDAR_STEPPER_DISTANCE ** 2) - (2*LIDAR_STEPPER_DISTANCE*x_distance*math.cos(math.radians(z_angle)))
    sin_g = (math.sin(math.radians(z_angle)) / math.sqrt(z_square)) * x_distance
    g_value_radient = math.asin(sin_g)
    g_value_degree = math.degrees(g_value_radient)
    print(f"Turret angle : ",g_value_degree)
    return g_value_degree

def calculate_turret_angel_difference(last_angle:float, current_angle:float):
    if last_angle == -(current_angle):
        angle_diff = last_angle + current_angle
    else:
        angle_diff = last_angle - current_angle

    return angle_diff