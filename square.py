class Square:
    # Constructor
    def __init__(self, color):
        self.color = color
        self.probability = 0    # Probability is 0 at very start, and should not be changed for BlACK squares
        self.vertical_neighbors = []
        self.horizontal_neighbors = []

    # Updates the probability that the EV3 is on this square
    def set_probability(self, new_probability):
        self.probability = new_probability


    # Sets the neighbors of this square when the grid is initialized
    def set_neighbors(self, vertical_neighbors, horizontal_neighbors):
        self.vertical_neighbors = vertical_neighbors
        self.horizontal_neighbors = horizontal_neighbors
