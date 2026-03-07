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
