from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.reset()

    def reset(self):
        self.setheading(90)
        self.goto(0, -300)

    def move_up(self):
        self.setheading(90)
        self.forward(25)

    def move_down(self):
        self.setheading(270)
        self.forward(25)