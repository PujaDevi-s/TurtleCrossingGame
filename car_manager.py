from turtle import Turtle
import random

# Making different colors for the car
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Each car will start moving at this speed 
STARTING_MOVE_DISTANCE = 5

# Each car's speed will be increased at every level
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE    # Assigning the staring move distance

    def create_car(self):                          # creating a new car
        random_chance = random.randint(1,6)       # generating random number from 1 to 6

        # If the random number is 1 then a new car will be automatically created by system

        if random_chance == 1:
            new_car = Turtle("square")                        #  The car will be in square shape
            new_car.shapesize(stretch_wid=1, stretch_len=2)   # streching the square length
            new_car.penup()                                   # the turtle will create a line, so to avoid it the penup is kept
            new_car.color(random.choice(COLORS))              # choosing random color for car
            random_y = random.randint(-250, 250)              # the cars starting position randomly generated in y axis
            new_car.goto(300, random_y)                       # x axis is always at left end
            self.all_cars.append(new_car)                     # adding newly created car to the list

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)                     # turtle will be facing right side, so backward means forward
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT                    # increasing the car speed at each level
