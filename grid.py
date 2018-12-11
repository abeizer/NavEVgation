'''
Grid Class:

    A representation of the colored grid that EV3 will use for navigation

    | red   | blue  | green | red   |
    | green | green | red   | blue  |
    | red   | blue  | white | green |
    | green | red   | red   | blue  |

'''


from square import Square
from color import Color

class Grid:
    def __init__(self):
        # Create the grid of squares
        self.squares = [
            [ Square(Color.RED, 0, 0), Square(Color.BLUE, 0, 1), Square(Color.GREEN, 0, 2), Square(Color.RED, 0 , 3) ],
            [ Square(Color.GREEN, 1, 0), Square(Color.GREEN, 1, 1), Square(Color.RED, 1, 2), Square(Color.BLUE, 1, 3) ],
            [ Square(Color.RED, 2, 0), Square(Color.BLUE, 2, 1), Square(Color.WHITE, 2, 2), Square(Color.GREEN, 2, 3) ],
            [ Square(Color.GREEN, 3, 0), Square(Color.RED, 3, 1), Square(Color.RED, 3, 2), Square(Color.BLUE, 3, 3) ]
        ]

        # Update every square in the grid with its vertical and horizontal neighbors
        self.assign_neighbors()


    # At the very beginning of the program, we do not have any previous color data to compare
    # to the currently-observed colors.
    def determine_starting_position(self, front_color, back_color):
        viable_squares = []

        # for each square, check to see if its horizontal_neighbors or vertical_neighbors match the curent sensors readings
        # if the neighbors do not match up to the sensor readins, set that squares' probability to 0
        # if the neighbors match, then the square is a viable possibility.
        #   Add that square to a list of viable options
        for row in self.squares:
            for s in row:
                # If both neighbors do not match either this square's horizontal or vertical neighbors
                # then the robot cannot be on this square.
                # TODO: Should the '0' probability account for the chance that a sensor reads an incorrect color?
                if not s.neighbors_match(front_color, back_color):
                    s.set_probability(0.0)
                    continue
                else:
                    viable_squares.append(s)
        
        if(len(viable_squares) == 0):
            raise Exception("No viable options detected for starting square")

        for s in viable_squares:
            s.set_probability(1/len(viable_squares))

        # if the list contains more than one square, then their probabilities will be the same for starting position.
        # so just return the first square in the list
        return viable_squares[0].row, viable_squares[0].column

    # This function will allow the EV3 to pass in the colors it sees in front of it and behind it
    # and compare them to the colors it saw in the last color checking phase.
    # Then the grid will update all of its squares with the probability that the EV3 is occupying that square
    def update_probabilities(self, front_color, back_color):
        # TODO
        return None
    
    # This function will be used within the grid class to get all the colors surrounding a square at squares[x][y]
    # The EV3 can be oriented in two directions: 
    #   1. With sensors seeing the neighbors above and below the square
    #   2. With the sensors seeing neighbors to the left and right of the square.
    #   Therefore, this function returns both sets of neighbors separately.
    def assign_neighbors(self):

        for row in range(0, 4):
            for column in range(0, 4): 
                vertical_neighbors = []
                horizontal_neighbors = []
        
                # This could be shortened to if(row == 0 oir row == 3)
                #   and if(column == 0 or column == 3)
                #   However, doing it this way makes it so that:
                #       vertical_neighbors[0] is always the top
                #       vertical_neighbors[1] is always the bottom
                #       horizontal_neighbors[0] is always the left
                #       horizontal_neighbors[1] is always the right
                if(row == 0):
                    # Right now, the Black border is represented by a Black square
                    # Because these squares arent a part of the actual Grid, I believe
                    # they won't mess with any of the computations. However, we definitely
                    # need to be mindful of this or find a better way to represent the border
                    vertical_neighbors.append(Square(Color.BLACK)) 
                else:
                    vertical_neighbors.append(self.squares[row-1][column])

                if(row == 3):
                    vertical_neighbors.append(Square(Color.BLACK))
                else:
                    vertical_neighbors.append(self.squares[row+1][column])

                if(column == 0):
                    horizontal_neighbors.append(Square(Color.BLACK))
                else:
                    horizontal_neighbors.append(self.squares[row][column-1])
                
                if(column == 3):
                    horizontal_neighbors.append(Square(Color.BLACK))
                else:
                    horizontal_neighbors.append(self.squares[row][column+1])
                
                self.squares[row][column].set_neighbors(vertical_neighbors, horizontal_neighbors)
                self.squares[row][column].set_probability(1.0/16)
