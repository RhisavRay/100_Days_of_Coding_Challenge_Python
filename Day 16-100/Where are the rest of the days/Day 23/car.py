from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape('square')
        self.shapesize(1, 2)
        self.dist = random.randint(5, 20)

    def color_random(self):
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(self.dist)