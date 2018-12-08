# NavEVgation
Lego EV3 Navigation using probabilistic localization

## Requirements
* [Lego Mindstorm EV3](https://www.lego.com/en-us/mindstorms/products/mindstorms-ev3-31313) with Light Sensors
* [EV3 Python](https://sites.google.com/site/ev3devpython/introduction)
* A square grid filled with colors as outlined under the _grid.py_ header

## Program Overview
### square.py
The Square class represents a single square on our grid. Each Square has a color and a probability. The probability is calculated by EV3 to determine how likely the robot is currently on top of that Square.

### grid.py
The grid holds a list of lists, named squares. Each list in squares represents a single row of the grid.

| index |   0   |   1   |   2   |   3   |
|-------|:-----:|:-----:|:-----:|:-----:|
| 0     |  Red  |  Blue | Green |  Red  |
| 1     | Green | Green |  Red  |  Blue |
| 2     |  Red  |  Blue | White | Green |
| 3     | Green |  Red  |  Red  |  Blue |

White represents the goal that EV3 is trying to navigate towards.

### color.py
The Color enum is used within the Grid and Square for logic that deals with comparison between expected colors from Grid.squares and actual colors detected by EV3's light sensors.

## Authors
* [Abby Beizer](https://github.com/abeizer)
* [Brandon Campbell](https://github.com/branlcampbell)
* [Jason Fazio](https://github.com/jayfaz)
* [Joseph Hammer](https://github.com/Invisy)
* [Steve MacDonald](https://github.com/MacDonaldSteve)
* [Katie Prochilo](https://github.com/KatieProchilo)
