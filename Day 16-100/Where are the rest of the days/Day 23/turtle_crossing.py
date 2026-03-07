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

game_is_on = True

def game_loop():
    global game_is_on
    if game_is_on:
        pass

screen.exitonclick()