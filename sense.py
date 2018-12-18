'''
Authors:
    - Katie Prochilo
    - Brandon Campbell
'''


from ev3dev.ev3 import *
from color import Color


front_cs = ColorSensor('in1')
back_cs = ColorSensor('in2')
front_cs.mode = 'COL-COLOR'
back_cs.mode = 'COL-COLOR'


def get_front_enum():
    val = front_cs.value()
    if (val == 0):
        return Color.BLACK
    return Color(val)


def get_rear_enum():
    val = back_cs.value()
    if (val == 0):
        return Color.BLACK
    return Color(val)
