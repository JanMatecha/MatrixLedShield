from machine import Pin
import time


pin = Pin(2, Pin.OUT)

for i in range(3):
    pin.value(0)
    print(pin.value())
    time.sleep(0.5)
    pin.value(1)
    print(pin.value())
    time.sleep(0.5)

