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

    def show_score(self):
        self.score.clear()
        self.score.write(f"Score: {self.score_value}", align="center", font=("Arial", 16, "normal"))

    def gain_score(self):
        self.score_value += 1
        self.show_score()

    def game_over(self):
        self.score.clear()
        self.score.write(f"GAME OVER  ---  Final Score: {self.score_value}", align="center", font=("Arial", 16, "normal"))