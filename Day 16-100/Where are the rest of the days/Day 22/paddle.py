from turtle import Turtle

LEFT_X = -400
RIGHT_X = 400

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.shape("square")
        self.shapesize(5, 0.5)
        self.color("white")
        self.penup()
        if self.side == "left":
            self.goto(LEFT_X, 0)
        else:
            self.goto(RIGHT_X, 0)

    def move_up(self):
        if self.ycor() + 50 < 295:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() - 50 > -295:
            self.goto(self.xcor(), self.ycor() - 20)