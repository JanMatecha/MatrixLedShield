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