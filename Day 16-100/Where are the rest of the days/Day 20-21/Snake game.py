from turtle import Turtle, Screen
import time

screen = Screen()
# Make screen background black
screen.bgcolor("black")

# TODO 1: Create the snake

turtles = []
init_pos = [-20, 0, 20]
screen.tracer(0)

for i in range(3):
    turtle = Turtle()
    turtle.shape("square")
    turtle.color("white")
    turtle.up()
    turtle.goto(init_pos[i], 0)
    turtles.append(turtle)

screen.update()

# TODO 2: Make the snake move forward till GAME OVER (This logic to be added later)



# TODO 3: Use arrow keys to change the heading of the snake



# TODO 4: Make food dots in random location on the screen



# TODO 5: Upon eating the food, another food dot appears at random on the screen



# TODO 6: Make the snake grow upon eating the food



# TODO 7: Add score feature



# TODO 8: Add the GAME OVER logic (Hitting wall or biting own tail)



screen.exitonclick()