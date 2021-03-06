from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.start_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.start_speed)

    def speed_up(self):
        self.start_speed += MOVE_INCREMENT
