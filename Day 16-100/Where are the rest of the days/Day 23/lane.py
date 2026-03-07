from turtle import Turtle
from car import Car
import random


class Lane(Turtle):
    def __init__(self, side, y):
        super().__init__()
        self.side = side
        self.car = Car()
        self.hideturtle()
        self.side = side
        self.y = y
        self.car_setup()

    def car_setup(self):
        self.car.color_random()
        self.car.dist = random.randint(5, 20)
        if self.side == "L":
            self.car.goto(-320, self.y)
            self.car.setheading(0)
        elif self.side == "R":
            self.car.goto(320, self.y)
            self.car.setheading(180)