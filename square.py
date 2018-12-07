class Square:
    # Constructor
    def __init__(self, color):
        self.color = color
        self.probability = 0    # Probability is 0 at very start.

    # Updates the probability that the EV3 is on this square
    def set_probability(self, new_probability):
        self.probability = new_probability
    
    
