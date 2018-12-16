#!/usr/bin/python3

from grid import Grid
from color import Color
# from drive import *
# from sense import *


def main():
    grid = Grid()   # EV3's internal representation of the colored grid.

    # Confirm that we can print out the color of each square in the grid
    #print_init_grid_probs(grid)

    
    # Test update_probabilities
    # Pretend we start on square(0,1) and are moving from square(0,1) to square(0,2)
    # And then from square(0,2) to square(1,2)

    x, y = grid.determine_starting_position(Color.GREEN, Color.RED)
    print("[", x, ",", y, "]")
    print(grid.squares[x][y].color, " --> ", grid.squares[x][y].probability)
    print()
    x, y = grid.update_probabilities(Color.GREEN, Color.RED, Color.BLUE, Color.RED)
    print("[", x, ",", y, "]")
    print(grid.squares[x][y].color, " --> ", grid.squares[x][y].probability)
    print()
    # EV3 would have to rotate here, which is why the colors change from blue/red to black/red
    x, y = grid.update_probabilities(Color.BLACK, Color.RED, Color.GREEN, Color.WHITE)
    print("[", x, ",", y, "]")
    print(grid.squares[x][y].color, " --> ", grid.squares[x][y].probability)
    print()

    
def print_init_grid_probs(myGrid):
    for row in myGrid.squares:
        for s in row:
            print(s.color, " --> ", s.horizontal_neighbors[0].color, " ", s.horizontal_neighbors[1].color,
                  " ^ ", s.vertical_neighbors[0].color, " ", s.vertical_neighbors[1].color, " <-- ", s.probability)
            print(s.horizontal_neighbors[0].probability)
    print()

    

def drive_example():
    # Show basic capabilities from drive.py, some unfinished
    # turn_left()
    # turn_right()
    # move_straight()
    # stop()

if __name__ == '__main__':
    main()
