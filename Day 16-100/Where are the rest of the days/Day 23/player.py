from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0, -280)
        self.lt(90)
        self.reset()
