from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(-250, 280)
        self.score = 1