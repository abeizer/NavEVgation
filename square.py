class Square:
    # Constructor
    def __init__(self, color, row=-1, column=-1):
        self.color = color
        # Probability is 0 at very start, and should not be changed for BlACK squares
        self.probability = 0.0
        self.row = row
        self.column = column
        self.vertical_neighbors = []
        self.horizontal_neighbors = []

    # Updates the probability that the EV3 is on this square
    def set_probability(self, new_probability):
        self.probability = new_probability

    # Sets the neighbors of this square when the grid is initialized

    def set_neighbors(self, vertical_neighbors, horizontal_neighbors):
        self.vertical_neighbors = vertical_neighbors
        self.horizontal_neighbors = horizontal_neighbors

    # returns true if the front and back sensors each see colors that both match either the horizontal or vertical neighbors
    def neighbors_match(self, front_color, back_color):
        if(self.horizontal_neighbors[0].color == front_color):
            if(self.horizontal_neighbors[1].color == back_color):
                return True

        if(self.horizontal_neighbors[1].color == front_color):
            if(self.horizontal_neighbors[0].color == back_color):
                return True

        if(self.vertical_neighbors[0].color == front_color):
            if(self.vertical_neighbors[1].color == back_color):
                return True

        if(self.vertical_neighbors[1].color == front_color):
            if(self.vertical_neighbors[0].color == back_color):
                return True

        return False
