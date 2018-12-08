'''
This Color enum is used for consistency throughout the rest of the program.
Any values used to represent the colors will all agree with this enum.

We can change this later from ints to the rgb values that represent each color, if that seems like a good idea
'''

from enum import Enum


class Color(Enum):
    BLACK = 0
    WHITE = 1
    RED = 2
    BLUE = 3
    GREEN = 4
