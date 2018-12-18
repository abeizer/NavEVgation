'''
Attributes:
    -

Authors:
    - Katie Prochilo
    - Brandon Campbell
'''

from ev3dev.ev3 import *


front_cs = ColorSensor('in1')
back_cs = ColorSensor('in2')
front_cs.mode = 'RGB-RAW'
back_cs.mode = 'RBG-RAW'

def get_rgb(sensor):
    return sensor.value()
