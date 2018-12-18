#!/usr/bin/python3

from grid import Grid
from color import Color
from drive import Drive
from sense import *


def main():
    """
    Entry point to the progrm.

    Creates a new instance of the physical grid, then the
    robot uses that grid to navigate to the white square.

    Authors: Abby Beizer, Katie Prochilo
    """
    # EV3's internal representation of the colored grid.
    grid = Grid()
    # Navigate the robot to the end square
    navigate_to_white(self, grid)


def navigate_to_white(self, myGrid):
    """
    This function will walk through a sample run of the
    program, but will hardcode in the actual movement.

    Authors: Katie Prochilo
    """
    # Get the current values the color sensor sees
    front = front_cs
    back = back_cs
    front_val = get_rgb(front)
    back_val = get_rgb(back)

    # Get the best guess of the robot's starting position as row,
    # col
    start_row, start_col = myGrid.determine_starting_position(
        self, front_val, back_val)
    # Check that row and col are in range
    if (start_row > 3 or start_row < 0 or start_col > 3 or start_col < 0):
        print("The starting row or column is out of range.")
        return

    # Let's say the robot starts at row 0, col 1.
    print("Here's how the robot starts:")
    # Here's the grid showing where the robot is at
    print_grid_coord(myGrid, start_row, start_col)
    # Now what's the first move to find white
    get_next_move(self, myGrid, start_row, start_col)


def get_next_move(self, myGrid, row, col):
    """
    Before this function is called the first time, the program
    will have a single square where it thinks it is most likely
    to be.

    The function will print the grid using print_grid_options()
    before also printing and executing the next move, i.e.
    "Go left."

    The END square is hard coded at coordinate (2,2)

    Authors: Katie Prochilo, Jason Fazio
    """
    # The robot is on white. Run is over.
    if (row == 2 and col == 2):
        print("The robot is on white. THE END.")
        return
    # The robot is on the proper row but not column.
    elif (row == 2):
        if (col > 2):
            col -= 1
            print("\nGo left:")
            self.turn_left()
            self.rotate_right()

        else:
            col += 1
            print("\nGo right:")
            self.turn_right()
            self.rotate_left()
    # The robot is below the goal.
    elif (row > 2):
        row -= 1
        print("\nGo up:")
        self.advance_one_block()
    # The robot is above the goal.
    else:
        row += 1
        print("\nGo down:")
        self.advance_backwards_one_block()
    print_grid_coord(myGrid, row, col)
    get_next_move(self, myGrid, row, col)


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


def print_probs(grid):
    """
    Authors: Abby Beizer
    """
    print(grid.determine_starting_position(Color.GREEN, Color.RED))
    print(grid.squares[0][1].color, " --> ", grid.squares[0][1].probability)

    x, y = grid.determine_starting_position(Color.GREEN, Color.RED)
    print("[", x, ",", y, "]")
    print(grid.squares[x][y].color, " --> ", grid.squares[x][y].probability)
    print()
    x, y = grid.update_probabilities(
        Color.GREEN, Color.RED, Color.BLUE, Color.RED)
    print("[", x, ",", y, "]")
    print(grid.squares[x][y].color, " --> ", grid.squares[x][y].probability)
    print()
    # EV3 would have to rotate here, which is why the colors
    # change from blue/red to black/red.
    x, y = grid.update_probabilities(
        Color.BLACK, Color.RED, Color.GREEN, Color.WHITE)
    print("[", x, ",", y, "]")
    print(grid.squares[x][y].color, " --> ", grid.squares[x][y].probability)
    print()


def print_init_grid_probs(myGrid):
    """
    Authors: Abby Beizer
    """
    # Confirm that we can print out the color of each square in
    # the grid.
    for row in myGrid.squares:
        for s in row:
            print(s.color, " --> ", s.horizontal_neighbors[0].color, " ", s.horizontal_neighbors[1].color,
                  " ^ ", s.vertical_neighbors[0].color, " ", s.vertical_neighbors[1].color, " <-- ", s.probability)
            print(s.horizontal_neighbors[0].probability)
    print()


if __name__ == '__main__':
    main()
