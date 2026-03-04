from turtle import Turtle

class ScoreCard:
    def __init__(self):
        self.score = Turtle()
        self.score_setup()
        self.score_value = 0
        self.show_score()

    def score_setup(self):
        self.score.hideturtle()
        self.score.up()
        self.score.goto(0, 310)
        self.score.color("white")


    def gain_score(self):
        self.score += 1
