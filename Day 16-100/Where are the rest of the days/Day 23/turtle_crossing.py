from turtle import Turtle, Screen
from player import Player


screen = Screen()
screen.setup(600, 600)

player = Player()

game_is_on = True

def game_loop():
    global game_is_on
    if game_is_on:
        pass

screen.exitonclick()