#!/usr/bin/python3

'''
Attributes:
    -

Authors:
    - Katie Prochilo
    - Jason Fazio

TODO:
    - Create the following functions:
        * turnLeft()
        * turnRight()
        * advanceOneBlock()
'''

from ev3dev.ev3 import *


left_motor = LargeMotor('outC')
right_motor = LargeMotor('outB')


def turnLeft():
    """
    Tested with Katie and Steve's 2nd robot on the poster
    grid on hardwood floor.

    Turns the robot exactly 90 DEGREES to the LEFT, exactly
    in place.
    """
	left_motor.run_to_rel_pos(position_sp=190, speed_sp=300, stop_action="brake")
    right_motor.run_to_rel_pos(position_sp=-190, speed_sp=300, stop_action="brake")
    print("Will eventually turn left.")


def turnRight():
    """
    Tested with Katie and Steve's 2nd robot on the poster
    grid on hardwood floor.

    Turns the robot exactly 90 DEGREES to the RIGHT, exactly
    in place.
    """
	left_motor.run_to_rel_pos(position_sp=-190, speed_sp=300, stop_action="brake")
    right_motor.run_to_rel_pos(position_sp=190, speed_sp=300, stop_action="brake")
    print("Will eventually turn right.")


def stop():
    """
    Both motors stop and both wheels brake to a stop.
    """
    left_motor.stop()
    right_motor.stop()


def advanceOneBlock():
    """
    The robot advances one block, or 3.5 inches, or until its
    colors sensors see a change.
    """
    print("Will eventually advance one block.")
