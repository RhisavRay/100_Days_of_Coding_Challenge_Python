from random import randint
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
# Change the shape to that of a turtle
timmy.shape("turtle")
# Change the color of the turtle
timmy.color("red")

# colors = ["red", "yellow", "green", "blue", "purple", "cornflower blue", "orange", "pink", "green yellow", "dark orange"]

# Move the tutle 100 units to the front
# the basic forward, backward, left and right commands have shorthand versions as well. They work exactly the same way.
# Just they are smaller commands to write
# timmy.forward(100)
# Turn Timmy to the right. This function takes degrees as the argument
# timmy.left(90)


# Make Timmy draw a square

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

# Now instead of all the previous lines, we can just use a loop as well
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# Timmy draws a dashed line

# timmy.up()
# timmy.backward(500)
# timmy.down()
# for _ in range(50):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()


# Timmy draws triangle, sqaure, pentagon, hexagon, and so on till 10 sides

# timmy.up()
# timmy.right(90)
# timmy.backward(200)
# timmy.left(90)
# timmy.backward(50)
# timmy.down()
#
# for i in range(3, 11):
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.rt(360/i)


# Timmy draws a random walk

# screen.colormode(255)
# timmy.width(10)
# timmy.speed(100)
#
# angles = [0, 90, 180, 270]
#
# for _ in range(100):
#     # timmy.color(random.choice(colors))
#     timmy.color((randint(1, 255), randint(1, 255), randint(1, 255)))
#     timmy.left(random.choice(angles))
#     timmy.forward(30)


# Timmy draws a spirograph

# screen.colormode(255)
# timmy.width(2)
# timmy.speed(100)
# for _ in range(36):
#     timmy.color((randint(1, 255), randint(1, 255), randint(1, 255)))
#     timmy.circle(100)
#     timmy.left(10)


# Timmy draws a million dollar piece of art
# screen.colormode(255)
# timmy.speed(300)
# timmy.up()
# timmy.back(150)
# timmy.rt(90)
# timmy.fd(150)
# timmy.lt(90)
# timmy.down()
# for _ in range(10):
#     for _ in range(10):
#         timmy.color((randint(1, 255), randint(1, 255), randint(1, 255)))
#         timmy.dot(10)
#         timmy.up()
#         timmy.forward(30)
#         timmy.down()
#     timmy.up()
#     timmy.back(300)
#     timmy.left(90)
#     timmy.fd(30)
#     timmy.right(90)
#     timmy.down()


# Makes the screen wait for a click before it closes
screen.exitonclick()