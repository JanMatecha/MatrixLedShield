import mled, time


class Example:

    def __init__(self):
        self.matrix = mled.driver(13, 14)
        self.matrix.clear()
        self.matrix.setIntensity(1)
        self.smer="S"   # S, V, J, Z
        self.pozice_x = 0
        self.pozice_y = 0


    def test(self):
        for x in range(8):
            for y in range(8):
                self.matrix.pixel(x, y, self.matrix.ON)
                self.matrix.display()
                time.sleep(1)
                self.matrix.pixel(x, y, self.matrix.OFF)
                self.matrix.display()

    def set_pozice(self,x,y):
        self.pozice_x = x
        self.pozice_y = y
        self.matrix.clear()
        self.matrix.pixel(x, y, self.matrix.ON)
        self.matrix.display()

    def posun(self, dx, dy):
        self.matrix.pixel(self.pozice_x, self.pozice_y, self.matrix.OFF)
        if dx > 0 and self.pozice_x < 7:
            self.pozice_x = self.pozice_x + dx
        elif dx > 0 and self.pozice_x >= 7:
            self.pozice_x = self.pozice_x - 7 + dx
        elif dx < 0 and self.pozice_x > 0:
            self.pozice_x = self.pozice_x  + dx
        elif dx < 0 and self.pozice_x <= 0:
            self.pozice_x = self.pozice_x + 7 + dx


        if dy > 0 and self.pozice_y < 7:
            self.pozice_y = self.pozice_y + dy
        elif dy > 0 and self.pozice_y >= 7:
            self.pozice_y = self.pozice_y - 7 + dy
        elif dy < 0 and self.pozice_y > 0:
            self.pozice_y = self.pozice_y  + dy
        elif dy < 0 and self.pozice_y <= 0:
            self.pozice_y = self.pozice_y + 7 + dy


        self.matrix.pixel(self.pozice_x, self.pozice_y, self.matrix.ON)
        self.matrix.display()

    def krok(self, smer):
        if smer == "S":
            self.posun(0,1)
        if smer == "J":
            self.posun(0,-1)
        if smer == "V":
            self.posun(1,0)
        if smer == "Z":
            self.posun(-1,0)

        pass


app = Example()
#app.test()
app.set_pozice(4,4)


from machine import Pin


pin = Pin(0, Pin.IN,  Pin.PULL_UP)
print(pin.value())

while True:
    if pin.value() == 0:
        app.krok("S")
        time.sleep_ms(500)
    else:
        app.krok("J")
        time.sleep_ms(500)




"""
while True:
    app.krok("V")
    time.sleep_ms(500)
    app.krok("V")
    time.sleep_ms(500)
    app.krok("S")
    time.sleep_ms(500)
    app.krok("S")
    time.sleep_ms(500)

    app.krok("Z")
    time.sleep_ms(500)
    app.krok("Z")
    time.sleep_ms(500)

    app.krok("J")
    time.sleep_ms(500)
    app.krok("J")
    time.sleep_ms(500)

"""