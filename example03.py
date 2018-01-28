import mled, time

matrix = mled.driver(13, 14)


def setFrame(frame):
    matrix.frame(frame)
    matrix.display()



matrix.clear()
frame = 0x00367F7F3E1C0800
frame = 0x00183C5A18181800
frame = 0x001818185A3C1800
frame = 0x0008047E7E040800
frame = 0x0010207E7E201000
setFrame(frame)



