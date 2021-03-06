'''
Attributes:
    - left_motor - powers the left wheel
    - right_motor - powers the right wheel

Authors:
    - Katie Prochilo
    - Jason Fazio
    - Brandon Campbell
'''

from ev3dev.ev3 import *
from time import sleep

left_motor = LargeMotor('outC')
right_motor = LargeMotor('outB')


def turn_left():
    """
    Turns the robot 90 degrees to the left relative to the
    robot's center. In this context, the center is the robot's
    logic unit, which should be in the middle of two squares
    that each have one sensor over top of them.

    Note: This method is fairly consistent, but the robot's
    motors sometimes do throw off the correct positioning of
    where the robot should actually end up, so minor adjustments
    may need to be made if this causes problems.

    Authors and testers: Jason Fazio, Joe Hammer, Brandon Campbell
    """
    left_motor.run_to_rel_pos(
        position_sp=-150, speed_sp=200, stop_action="brake")
    right_motor.run_to_rel_pos(
        position_sp=-150, speed_sp=200, stop_action="brake")
    left_motor.wait_while('running')
    right_motor.wait_while('running')
    sleep(1.0)

    right_motor.run_to_rel_pos(
        position_sp=350, speed_sp=350, stop_action="brake")
    right_motor.wait_while('running')


def turn_right():
    """
    Turns the robot 90 degrees to the right relative to the
    robot's center. In this context, the center is the robot's
    logic unit, which should be in the middle of two squares
    that each have one sensor over top of them.

    Note: This method is fairly consistent, but the robot's
    motors sometimes do throw off the correct positioning of
    where the robot should actually end up, so minor adjustments
    may need to be made if this causes problems.

    Authors and testers: Jason Fazio, Joe Hammer, Brandon Campbell
    """
    left_motor.run_to_rel_pos(
        position_sp=-150, speed_sp=200, stop_action="brake")
    right_motor.run_to_rel_pos(
        position_sp=-150, speed_sp=200, stop_action="brake")
    left_motor.wait_while('running')
    right_motor.wait_while('running')
    sleep(1.0)

    left_motor.run_to_rel_pos(
        position_sp=350, speed_sp=350, stop_action="brake")
    left_motor.wait_while('running')


def stop():
    """
    Both motors stop and both wheels brake to a stop.

    Authors and testers: Katie Prochilo
    """
    left_motor.stop()
    right_motor.stop()


def advance_one_block():
    """
    The robot advances exactly one block. This has been tested
    on hardwood and consistently moves it the required amount
    of distance so that it is in the same position relative to
    the square that it just moved from.

    Authors: Brandon Campbell
    """
    left_motor.run_to_rel_pos(
        position_sp=175, speed_sp=175, stop_action="brake")
    right_motor.run_to_rel_pos(
        position_sp=175, speed_sp=175, stop_action="brake")

    # Allow both motors to finish their movements
    left_motor.wait_while('running')
    right_motor.wait_while('running')


def advance_backwards_one_block():
    """
    The robot does the same as advance one block
    only in the negative direction
    this will be easier than turning around.

    Authors: Jason Fazio, Joe Hammer
    """
    left_motor.run_to_rel_pos(
        position_sp=-175, speed_sp=175, stop_action="brake")
    right_motor.run_to_rel_pos(
        position_sp=-175, speed_sp=175, stop_action="brake")

    # Allow both motors to finish their movements
    left_motor.wait_while('running')
    right_motor.wait_while('running')
