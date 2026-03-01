from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
tim = Turtle()

# Here we are going to learn about event listeners
# screen.listen()

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

"""
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
"""


# Make turtle race

"""

What I did wrong here was that I was trying to manipulate the speed of the turtles. It isn't that it was a wrong approach. But rather it
was missing a key portion. I just changed the speed. But the forward movement wasn't being made 

# Set up the dimensions of the screen
screen.setup(width=500, height=400)
screen.colormode(255)
turtles = []
y_coords = [-75, -45, -15, 15, 45, 75]
for i in range(6):
    tim = Turtle()
    tim.color((randint(1, 255), randint(1, 255), randint(1, 255)))
    tim.up()
    tim.goto(x = -240, y = y_coords[i])
    turtles.append(tim)

reached = False

def check_if_reached():
    global reached
    for turtle in turtles:
        turtle.speed(randint(50, 200))
        if turtle.xcor() >= 250:
            reached = True
            break

    if reached:
        screen.exitonclick()
    else:
        screen.ontimer(check_if_reached, 2000)
"""

screen.setup(width=500, height=400)
race_is_on = False
turtles = []
y_coords = [-75, -45, -15, 15, 45, 75]
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

for i in range(6):
    tim = Turtle()
    tim.color(colors[i])
    tim.up()
    tim.goto(x = -240, y = y_coords[i])
    turtles.append(tim)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

if user_bet:
    race_is_on = True

while race_is_on:
    for tim in turtles:
        if tim.xcor() >= 230:
            winning_color = tim.pencolor()
            if user_bet == winning_color:
                print(f"You win! The {winning_color} turtle was the winner!")
            else:
                print(f"You lose! The {winning_color} turtle was the winner!")
            race_is_on = False
            break
        dist = randint(5, 20)
        tim.fd(dist)

screen.exitonclick()