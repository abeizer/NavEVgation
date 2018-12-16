#!/usr/bin/python3

'''
Attributes:
    -

Authors:
    - Katie Prochilo
    - Brandon Campbell

TODO:
    - Decide how exactly we want to measure and track color
    - Create the following functions:
        * get_rgb()
        * is_over_color(color_measurement, current_measurement)
    - Test the following functions:
'''

from ev3dev.ev3 import *


front_cs = ColorSensor('in1')
back_cs = ColorSensor('in2')
front_cs.mode = 'RGB-RAW'
back_cs.mode = 'RBG-RAW'
