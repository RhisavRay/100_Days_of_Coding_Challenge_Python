from turtle import Turtle, Screen

timmy = Turtle()
# Change the shape to that of a turtle
timmy.shape("turtle")
# Change the color of the turtle
timmy.color("red")

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
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

screen = Screen()
# Makes the screen wait for a click before it closes
screen.exitonclick()