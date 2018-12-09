class Square:
    # Constructor
    def __init__(self, color):
        self.color = color
        self.probability = 0    # Probability is 0 at very start.
        self.x = 0
        self.y = 0
        self.nextToList = []

    # Updates the probability that the EV3 is on this square
    def set_probability(self, new_probability):
        self.probability = new_probability
    def setCoord(self, x, y):
    	self.x = x
    	self.y = y
    def setNextTo(self, other):
    	self.nextToList.append(other)
    def isNextTo(self, color): # takes in a color, returns true if it's next to this tile
    	if len(self.nextToList) == 0: # make sure we have at least one thing in the list
    		return false
    	for c in nextToList:
    		if (c.color == color):
    			return true
    	return false # return false after going through loop if it fails
    
    
