#!/usr/bin/python3

'''
Attributes:
    - left_motor - powers the left wheel
    - right_motor - powers the right wheel

Authors:
    - Katie Prochilo
    - Jason Fazio
    - Brandon Campbell

TODO:
    - Create the following functions:
        * advanceOneBlock()
    - Convert move_straight() to drive based on distance,
    rather than a certain amount of time.
'''

from ev3dev.ev3 import *


left_motor = LargeMotor('outC')
right_motor = LargeMotor('outB')


def turn_left():
    """
    Turns the robot exactly 90 DEGREES to the LEFT, exactly
    in place.

    Authors and testers: Jason Fazio, Brandon Campbell
    """
    left_motor.run_to_rel_pos(
        position_sp=190, speed_sp=300, stop_action="brake")
    right_motor.run_to_rel_pos(
        position_sp=-190, speed_sp=300, stop_action="brake")


def turn_right():
    """
    Turns the robot exactly 90 DEGREES to the RIGHT, exactly
    in place.

    Authors and testers: Jason Fazio, Brandon Campbell
    """
    left_motor.run_to_rel_pos(
        position_sp=-190, speed_sp=300, stop_action="brake")
    right_motor.run_to_rel_pos(
        position_sp=190, speed_sp=300, stop_action="brake")


def stop():
    """
    Both motors stop and both wheels brake to a stop.

    Authors and testers: Katie Prochilo
    """
    left_motor.stop()
    right_motor.stop()


def move_straight():
    """
    TODO: Right now this is timed driving. It needs to be
    converted to inches.

    For speed to be sp=700, each wheel needs 50% of that speed

    Authors and testers: Katie Prochilo
    """
    left_motor.run_timed(time_sp=200, speed_sp=200)
    right_motor.run_timed(time_sp=200, speed_sp=200)

    # Allow motors to finish their movements
    left_motor.wait_while('running')
    right_motor.wait_while('running')


def advance_one_block():
    """
    TODO: Still needs to be written.

    The robot advances one block, or 3.5 inches, or until its
    colors sensors see a change.

    The robot will check halfway through, at 1.75 inches, to see
    if it is over the black border on the grid.

    Authors: TODO
    """
    print("Will eventually advance one block.")
