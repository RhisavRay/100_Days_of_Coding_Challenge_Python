from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(-250, 280)
        self.score = 1

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align='center', font=('Courier', 14, 'normal'))

    def gain_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 250)
        self.write(f"GAME OVER\nLevel: {self.score}", align='center', font=('Courier', 14, 'normal'))