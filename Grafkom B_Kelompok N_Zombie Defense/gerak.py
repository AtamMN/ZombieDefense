from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import Zombie_Normal
import Zombie_Mini


def posisi_ZNormal():
    global y, a, pdh
    y = 5
    a = 1
    pdh = random.randrange(-22, 10)


def posisi_ZMini():
    global y, a, pdhm
    y = 5
    a = 1
    pdhm = random.randrange(-29, 6)


def kanvas_normal():
    global y, a, pdh
    if y >= -45:
        y -= a
        Zombie_Normal.canvas(pdh, y)
    else:
        y = y
        posisi_ZNormal()
    # print(y)


def kanvas_mini():
    global y, a, pdhm
    if y >= -45:
        y -= a
        Zombie_Mini.canvas(pdhm, y)


posisi_ZNormal()
posisi_ZMini()
