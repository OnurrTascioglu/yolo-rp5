import time
import gpiozero

step_pin = gpiozero.OutputDevice(21)
direction_pin = gpiozero.OutputDevice(20)

step_pin.off()

steps = 100

print("Single coil steps")
print("Steps: ", steps)
direction_pin.on()
for i in range(steps):
    print("Moving direction 0," , i)
    step_pin.on()
    time.sleep(0.02)
    step_pin.off()
    time.sleep(0.02)

print("Steps: ", steps)
direction_pin.off()
for i  in range(steps):
    print("Moving direction 1," , i)
    step_pin.on()
    time.sleep(0.02)
    step_pin.off()
    time.sleep(0.02)
