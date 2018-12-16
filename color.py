'''
This Color enum is used for consistency throughout the rest of the program.
Any values used to represent the colors will all agree with this enum.

We can change this later from ints to the rgb values that represent each color, if that seems like a good idea
'''

from enum import Enum


class Color(Enum):
    BLACK = 1
    BLUE = 2
    GREEN = 3
    RED = 5
    WHITE = 6
