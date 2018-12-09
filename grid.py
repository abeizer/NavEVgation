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
import math

class Grid:  
    def __init__(self):
        self.squares = [ 
            [ Square(Color.RED), Square(Color.BLUE), Square(Color.GREEN), Square(Color.RED) ],
            [ Square(Color.GREEN), Square(Color.GREEN), Square(Color.RED), Square(Color.BLUE) ],
            [ Square(Color.RED), Square(Color.BLUE), Square(Color.WHITE), Square(Color.GREEN) ],
            [ Square(Color.GREEN), Square(Color.RED), Square(Color.RED), Square(Color.BLUE) ]
        ]
        self.shortList = []

    def setSquares(self): # set up the squares for their coords and what they are next to
        temp = len(self.squares) # assuming it's square, just length of rows is enough
        for i in range(0,temp): # each row
            for j in range(0,temp): # each column
                self.squares[i][j].setCoord(j,i) # column for x value, row for y value
        for i in range(0,temp): # each row
            for j in range(0,temp): # each column
                if (i > 0): # go through each square, adding sqaures they are next to assuming they are not on the edge
                    self.squares[i][j].setNextTo(self.squares[i-1][j])
                if (i < (temp-1)):
                    self.squares[i][j].setNextTo(self.squares[i+1][j])
                if (j > 0):
                    self.squares[i][j].setNextTo(self.squares[i][j-1])
                if (j < (temp-1)):
                    self.squares[i][j].setNextTo(self.squares[i][j+1])
        for r in self.squares:
            for c in r:
                self.shortList.append(c) # instantiate our list of where we can possibly be

    def relist(self, that): # takes in a color that we see and shortens our list
        tempList = []
        for r in self.shortList:
            if r.isNextTo(that):
                tempList.append(r)
        if len(tempList) == 0:
            print("Error, no matches found")
            return
        self.shortList = tempList # assuming all went well, reassign to our new shortened list

    def currentProb(self): # simple function to get our current probability of where we are
        return 1 / len(self.shortList)
