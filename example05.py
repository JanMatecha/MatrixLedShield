from machine import Pin
import time

while True:
    pin0 = Pin(0, Pin.IN,  Pin.PULL_UP)
    print("zmacknut PIN 0 (D3)", pin0.value())


