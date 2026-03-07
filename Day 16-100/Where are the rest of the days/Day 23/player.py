from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.reset()

    def reset(self):
        self.setheading(90)
        self.goto(0, -300)
