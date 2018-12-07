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
        self.squares = [ 
            [ Square(Color.RED), Square(Color.BLUE), Square(Color.GREEN), Square(Color.RED) ],
            [ Square(Color.GREEN), Square(Color.GREEN), Square(Color.RED), Square(Color.BLUE) ],
            [ Square(Color.RED), Square(Color.BLUE), Square(Color.WHITE), Square(Color.GREEN) ],
            [ Square(Color.GREEN), Square(Color.RED), Square(Color.RED), Square(Color.BLUE) ]
        ]

