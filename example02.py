from machine import Pin


pin = Pin(0, Pin.IN,  Pin.PULL_UP)
print(pin.value())


