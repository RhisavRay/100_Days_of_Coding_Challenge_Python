from turtle import Turtle

class ScoreCard:
    def __init__(self):
        self.score = Turtle()
        self.score.hideturtle()
        self.score.up()
        self.score.goto(0, 310)
        self.score.color("white")
        self.score_value = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.show_score()

    def show_score(self):
        self.score.clear()
        self.score.write(f"Score: {self.score_value}  High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def gain_score(self):
        self.score_value += 1
        self.show_score()

    def update_highscore(self):
        if self.score_value > self.high_score:
            self.high_score = self.score_value
        with open("data.txt", "w") as data:
            data.write(str(self.high_score))
        self.score_value = 0
        self.show_score()

    def game_over(self):
        self.score.clear()
        self.score.write(f"GAME OVER  ---  Your Score: {self.score_value}  Highscore: {self.high_score}", align="center", font=("Arial", 16, "normal"))