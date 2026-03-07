from turtle import Screen
from player import Player
from lane import Lane
from score import Score
import random


screen = Screen()
screen.setup(650, 650)
screen.tracer(0)
screen.listen()


player = Player()

directions = {"Up": False, "Down": False}

def key_press(key):
    directions[key] = True

def key_release(key):
    directions[key] = False

screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Down"), "Down")


game_is_on = True
easy_mode = 0

ycors = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
side = ["L"]
if not easy_mode:
    side.append("R")
lanes = []
for ycor in ycors:
    lane = Lane(random.choice(side), ycor)
    lanes.append(lane)


score = Score()


def game_loop():
    global game_is_on
    score.show_score()
    if game_is_on:
        pass

screen.exitonclick()