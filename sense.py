'''
Attributes:
    -

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
    return Color(front_cs.value())

def get_rear_enum():
    return Color(back_cs.value())
