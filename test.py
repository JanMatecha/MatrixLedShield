import mled, time

matrix = mled.driver(13, 14)
matrix.clear()
matrix.setIntensity(1)
x=1
y=1
matrix.pixel(x, y, matrix.ON)
matrix.display()

for x in range(8):
    for y in range(8):
        matrix.pixel(x, y, matrix.ON)
        matrix.display()

time.sleep(1)
matrix.clear()
matrix.display()

for x in range(8):
    matrix.pixel(x, x, matrix.ON)
    matrix.display()

time.sleep(1)
matrix.clear()
matrix.display()

frame = 0x00367F7F3E1C0800
#frame = 0x0000000000000000
matrix.frame(frame)
matrix.display()

time.sleep(1)
matrix.clear()
matrix.display()

def setFrame(frame):
    matrix.frame(frame)
    matrix.display()
