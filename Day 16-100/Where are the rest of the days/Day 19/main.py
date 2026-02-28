from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

# Here we are going to learn about event listeners
screen.listen()

# Let us declare a function which will be executed upon listening to an event

# def move_forwards():
#     tim.forward(100)

"""
This event listener will listen for a key release event. For this case, the above defined func will be executed upon the release of the
space bar
"""

# screen.onkey(move_forwards, "space")
"""
NOTE: Why we do not use () after the function name when we are passing it as an argument is because () triggers the function
We don't want that to happen before the function it's being called into does it
"""


# Here we will make turtle move with the WSAD keys

tim.speed(100)

def forward():
    tim.fd(10)

def backward():
    tim.back(10)

def left():
    tim.lt(5)

def right():
    tim.rt(5)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(clear, "c")


screen.exitonclick()