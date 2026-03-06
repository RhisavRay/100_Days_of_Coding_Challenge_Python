from turtle import Turtle


class GameScore(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        if side == "Left":
            self.goto(-40, 310)
        else:
            self.goto(40, 310)
        self.show_score()

    def show_score(self):
        self.write(f"{self.score}", align="center", font=("Arial", 20, "normal"))

    def gain_score(self):
        self.clear()
        self.score += 1
        self.show_score()