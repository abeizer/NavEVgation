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


def get_rgb(sensor):
    return Color(sensor.value())
