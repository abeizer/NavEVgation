#!/usr/bin/python3

from grid import Grid
from color import Color
#from drive import *
#from sense import *


def main():
    grid = Grid()   # EV3's internal representation of the colored grid.

    # Confirm that we can print out the color of each square in the grid
    #for row in grid.squares:
    #    for s in row:
            #print(s.color, " --> ", s.horizontal_neighbors[0].color, " ", s.horizontal_neighbors[1].color, " ^ ", s.vertical_neighbors[0].color, " ", s.vertical_neighbors[1].color, " <-- ", s.probability)
    #       print(s.horizontal_neighbors[0].probability)
        
    #    print()

    print(grid.determine_starting_position(Color.GREEN, Color.RED))
    print(grid.squares[0][1].color, " --> ", grid.squares[0][1].probability)

    # Show basic capabilities from drive.py, some unfinished
    #turn_left()
    #turn_right()
    #move_straight()
    #stop()

    

if __name__ == '__main__':
    main()
