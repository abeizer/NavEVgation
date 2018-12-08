#!/usr/bin/python3

from grid import Grid
from drive import *


def main():
    grid = Grid()   # EV3's internal representation of the colored grid.

    # Confirm that we can print out the color of each square in the grid
    for row in grid.squares:
        for s in row:
            print(s.color, " ")
        print()

    turnLeft()
    turnRight()
    advanceOneBlock()
    stop()


if __name__ == '__main__':
    main()
