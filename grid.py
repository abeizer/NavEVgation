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
            [ Square(Color.RED), Square(Color.BLUE), Square(Color.GREEN), Square(Color.RED) ],
            [ Square(Color.GREEN), Square(Color.GREEN), Square(Color.RED), Square(Color.BLUE) ],
            [ Square(Color.RED), Square(Color.BLUE), Square(Color.WHITE), Square(Color.GREEN) ],
            [ Square(Color.GREEN), Square(Color.RED), Square(Color.RED), Square(Color.BLUE) ]
        ]

        # Update every square in the grid with its vertical and horizontal neighbors
        self.assign_neighbors()


    # This function will allow the EV3 to pass in the colors it sees in front of it and behind it
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
