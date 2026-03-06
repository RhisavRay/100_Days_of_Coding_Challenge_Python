from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import GameScore


screen = Screen()
screen.setup(width=880, height=680)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)


border = Turtle()
border.penup()
border.goto(-410, -310)
border.pendown()
border.pencolor("white")
for _ in range(2):
    border.fd(820)
    border.left(90)
    border.fd(620)
    border.left(90)
border.hideturtle()


dashed_line = Turtle()
dashed_line.pensize(5)
dashed_line.up()
dashed_line.hideturtle()
dashed_line.color("white")
dashed_line.goto(0, 300)
dashed_line.setheading(270)
for _ in range(25):
    dashed_line.down()
    dashed_line.fd(12)
    dashed_line.up()
    dashed_line.fd(12)


left_paddle = Paddle("left")
right_paddle = Paddle("right")

keys = {"w": False, "s": False, "Up": False, "Down": False}

def key_press(key):
    keys[key] = True

def key_release(key):
    keys[key] = False

screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("s"), "s")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Down"), "Down")


left_score = GameScore("Left")
right_score = GameScore("Right")


ball = Ball()


game_is_on = True

def game_loop():
    global game_is_on
    if game_is_on:
        if keys["w"]: left_paddle.move_up()
        if keys["s"]: left_paddle.move_down()
        if keys["Up"]: right_paddle.move_up()
        if keys["Down"]: right_paddle.move_down()
        ball.move()
        if ball.xcor() > 400:
            left_score.gain_score()
            ball.ball_reset()
        elif ball.xcor() < -400:
            right_score.gain_score()
            ball.ball_reset()
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.wall_bounce()
        left_paddle_bounce = ball.xcor() > 385 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50
        right_paddle_bounce = ball.xcor() < -385 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50
        if left_paddle_bounce or right_paddle_bounce:
            ball.paddle_bounce()
        left_score.show_score()
        right_score.show_score()
        screen.update()
        screen.ontimer(game_loop, 16)

game_loop()

screen.exitonclick()