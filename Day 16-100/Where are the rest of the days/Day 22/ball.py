from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_reset()

    def ball_reset(self):
        self.goto(0, 0)
        rand_angle = random.choice([
            random.uniform(30, 60),
            random.uniform(120, 150),
            random.uniform(210, 240),
            random.uniform(300, 320)
        ])
        self.setheading(rand_angle)

    def move(self):
        self.fd(10)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(180 - self.heading())