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

def game_loop():
    global game_is_on
    if game_is_on:
        pass

screen.exitonclick()