from turtle import Turtle
STARTING_POSITION = (0, -280)     # creating the start position
MOVE_DISTANCE = 10               # each time user clicks the up arrow the speed of turtle
FINISH_LINE_Y = 280              # when user reaches the 280 in Y axis then that is the finish line

class Player(Turtle):           # creating the turtle player
    def __init__(self):
        super().__init__()
        self.shape("turtle")     
        self.setheading(90)     # making the turtle face upward
        self.penup()           # the pen is lifted up otherwise the turtle will draw a line
        self.color("green")     
        self.startingpoint()    # calling the starting point function at bottom

    def startingpoint(self):
        self.goto(STARTING_POSITION)   # turtle goes to the starting position 

    def up(self):
        self.forward(MOVE_DISTANCE)      # moving distance of the turtle
