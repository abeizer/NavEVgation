from grid import Grid

def main():
    grid = Grid()   # EV3's internal representation of the colored grid.
    grid.setSquares()

    # Confirm that we can print out the color of each square in the grid
    for row in grid.squares:
        for s in row:
            print(s.color, " ")
        print() 


if __name__ == '__main__':
    main()
