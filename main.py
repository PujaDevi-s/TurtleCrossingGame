from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# starting the game level from 1
level = 1

#Creating a screen
screen = Screen()
screen.setup(width=600, height=600) 
screen.tracer(0)

# creating the turtle
player1 = Player()

# creating the car
car_manager = CarManager()

# creating the scoreboard
scoreboard = Scoreboard(level)

# the screen will start to listen the key movement of the user
screen.listen()

# When user clicks the up key the player calls a function up in player.py file and user moves in up direction
screen.onkey(fun =player1.up, key="Up")
game_is_on = True

# the game will be true and becomes false when turtle crashes with the car
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()   # car is being created for each loop
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:     
        if car.distance(player1) < 20:   # checking the distance between turtle and any car is close
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing

    if player1.ycor() > 280:      # turtle reached the finishing point 
       level+=1                   # The level is increased
       car_manager.level_up()     # adding random cars in next stage
       player1.startingpoint()    # moving the turtle to the starting position
       scoreboard.text(level)     # changing the level message at top

screen.exitonclick()              # when user clicks on screen the screen will get close
                                  # if it is not given then the screen will not be opened and we cannot see anything in screen
