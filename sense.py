#!/usr/bin/python3

'''
Attributes:
    -

Authors:
    - Katie Prochilo

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


def get_rgb():
    print("This will eventually get the RGB values a sensory reads")


def is_over_color(color_measurement, current_measurement):
    print("This will eventually get the RGB values a sensory reads")
