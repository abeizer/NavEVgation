#!/usr/bin/python3

from grid import Grid
from color import Color
# from drive import *
# from sense import *


def main():
    grid = Grid()   # EV3's internal representation of the colored grid.

    # Confirm that we can print out the color of each square in the grid
    print_init_grid_probs(grid)

    print_grid_options(grid, 2, 2)

    print(grid.determine_starting_position(Color.GREEN, Color.RED))
    print(grid.squares[0][1].color, " --> ", grid.squares[0][1].probability)

    # Examples from various classes
    # drive_example()


def print_init_grid_probs(myGrid):
    # Confirm that we can print out the color of each square in the grid
    for row in myGrid.squares:
        for s in row:
            print(s.color, " --> ", s.horizontal_neighbors[0].color, " ", s.horizontal_neighbors[1].color,
                  " ^ ", s.vertical_neighbors[0].color, " ", s.vertical_neighbors[1].color, " <-- ", s.probability)
            print(s.horizontal_neighbors[0].probability)
    print()


# def drive_example():
    # Show basic capabilities from drive.py, some unfinished
    # turn_left()
    # turn_right()
    # move_straight()
    # stop()


def get_next_move(myGrid, row, col):
    """
    TODO: Still needs to be written.

    Before this function is called, the program will have a
    single square where it thinks it is most likely to be.

    The function will print the grid using print_grid_options()
    before also printing the next move, i.e. "Turn left."

    Finally, the function will call the proper drive function.

    Authors: Katie Prochilo
    """
    print(myGrid)


def print_grid_options(myGrid, myRow, myCol):
    """
    Prints a grid containing an 'X' in the square
    with coordinates (myRow, myCol)

    Authors: Katie Prochilo
    """
    str = ""
    for row in myGrid.squares:
        for s in row:
            if (s.column == 3):
                # Print special formatting for an end square
                if (s.row != myRow or s.column != myCol):
                    # Print a blank square
                    str += "|     |\n"
                else:
                    # The robot is here
                    str += "|  X  |\n"
            else:
                if (s.row != myRow or s.column != myCol):
                    # Print a blank square
                    str += "|     "
                else:
                    # The robot is here
                    str += "|  X  "
    print(str)


if __name__ == '__main__':
    main()
