from turtle import Turtle

class ScoreCard:
    def __init__(self):
        self.score = 0
        self.score = Turtle()
        self.score_setup()
        self.score_value = 0
        self.show_score()


    def gain_score(self):
        self.score += 1
