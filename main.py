#!/usr/bin/python3

from grid import Grid
from color import Color
# from sense import *


def main():
    grid = Grid()   # EV3's internal representation of the colored grid.

    # Confirm that we can print out the color of each square in the grid
    print_init_grid_probs(grid)

    # A simulation of the moves the robot will make
    move_sequence_example(grid)

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


def move_sequence_example(myGrid):
    """
    This function will walk through a sample run of the
    program, but will hardcode in the actual movement.

    Authors: Katie Prochilo
    """
    # Let's say the robot starts at row 0, col 1.
    print("Here's how the robot starts:")
    print_grid_coord(myGrid, 0, 1)
    # Now what's the first move to find white
    get_next_move(myGrid, 0, 1)
    # According to the algorithm, go down one row
    get_next_move(myGrid, 1, 1)
    # Now we're in the correct row, so go right
    get_next_move(myGrid, 1, 2)
    # We should find we're at the goal
    get_next_move(myGrid, 2, 2)


def get_next_move(myGrid, row, col):
    """
    TODO: For now this will print the move the robot will make
    next, but eventually it will actually call the drive
    function. To do this, the robot needs to know its orientation.

    Before this function is called, the program will have a
    single square where it thinks it is most likely to be.

    The function will print the grid using print_grid_options()
    before also printing the next move, i.e. "Turn left."

    The END square is hard coded at coordinate (2,2)

    Authors: Katie Prochilo
    """
    # The robot is on white. Run is over.
    if (row == 2 and col == 2):
        print("\nThe robot is on white. THE END:")
    # The robot is on the proper row but not column.
    elif (row == 2):
        if (col > 2):
            col -= 1
            print("\nGo left:")
        else:
            col += 1
            print("\nGo right:")
    # The robot is below the goal.
    elif (row > 2):
        row -= 1
        print("\nGo up:")
    # The robot is above the goal.
    else:
        row += 1
        print("\nGo down:")
    print_grid_coord(myGrid, row, col)


def print_grid_coord(myGrid, myRow, myCol):
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
