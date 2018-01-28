import mled, time
from machine import Pin


Pin0 = Pin(0, Pin.IN,  Pin.PULL_UP)
Pin2 = Pin(2, Pin.IN,  Pin.PULL_UP)
Pin4 = Pin(4, Pin.IN)
Pin5 = Pin(5, Pin.IN)

matrix = mled.driver(13, 14)


def setFrame(frame):
    matrix.frame(frame)
    matrix.display()



matrix.clear()
frame_srdce = 0x00367F7F3E1C0800
frame_nic = 0x0000000000000000
frame_sipka_nahoru = 0x00183C5A18181800
frame_sipka_dolu = 0x001818185A3C1800
frame_sipka_vlevo = 0x0008047E7E040800
frame_sipka_vpravo = 0x0010207E7E201000


frame = frame_nic
while True:

    if Pin0.value() == 0:
        frame = frame_sipka_nahoru
    elif Pin2.value() == 0:
        frame = frame_sipka_dolu
    elif Pin4.value() == 1:
        frame = frame_sipka_vpravo
    elif Pin5.value() == 1:
        frame = frame_sipka_vlevo


    setFrame(frame)

