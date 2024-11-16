from turtle import Turtle
# Giving Font Styles for Scoreboard
FONT = ("Courier", 24, "normal")

# creating a new scoreboard
class Scoreboard(Turtle):
    def __init__(self,level):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-140,260)   # position where the scoreboard to be displaced
        self.hideturtle()     # hiding the turtle image
        self.text(level)
        
    def text(self,level):
        self.clear()          # removing the previous level text
        self.write(f"Level: {level}", align="right", font=FONT)   # adding a new lable text
    
    def game_over(self):
        self.goto(0,0)       # going to the center
        self.write("Game Over", align="center", font=FONT)  # displaying game over text at center position
