import time
import gpiozero

step_pin = gpiozero.OutputDevice(21)
direction_pin = gpiozero.OutputDevice(20)

step_pin.off()

steps = 2000

print("Single coil steps")
print("Steps: ", steps)
direction_pin.on()
for _ in range(steps):
    step_pin.on()
    time.sleep(0.001)
    step_pin.off()
    time.sleep(0.001)

direction_pin.off()
for _ in range(steps):
    step_pin.on()
    time.sleep(0.001)
    step_pin.off()
    time.sleep(0.001)
