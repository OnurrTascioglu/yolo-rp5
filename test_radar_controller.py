import time
import gpiozero
from utils.constants import *

direction_pin_horizontal = gpiozero.OutputDevice(DIR_PIN_HOR)
step_pin_horizontal = gpiozero.OutputDevice(STEP_PIN_HOR)

direction_pin_horizontal.on()

step = 100
counter = 0
direction = True

def change_direction(direction):
    if direction == True:
        direction_pin_horizontal.off()
        direction = False
        return direction
    if direction == False:
        direction_pin_horizontal.on()
        direction = True
        return direction

while True:
    if counter == step:
        direction = change_direction(direction)
        print(direction)
        counter = 0
    step_pin_horizontal.on()
    time.sleep(0.001)
    step_pin_horizontal.off()
    time.sleep(0.001)
    counter = counter + 1
