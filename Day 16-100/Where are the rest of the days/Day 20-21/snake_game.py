from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_card import ScoreCard

screen = Screen()
screen.setup(width=680, height=680)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

food = Food()

score_card = ScoreCard()

border = Turtle()
border.penup()
border.goto(-310, -310)
border.pendown()
border.pencolor("white")
for _ in range(4):
    border.fd(620)
    border.left(90)
border.hideturtle()

game_is_on = True

def game_loop():
    global game_is_on
    if game_is_on:
        snake.move()
        if food.collision_detection(snake.head):
            score_card.gain_score()
            snake.grow_snake()
        if snake.wall_collision() or snake.bite_check():
            game_is_on = False
            score_card.update_highscore()
            score_card.game_over()
        screen.update()
        screen.ontimer(game_loop, 100)

game_loop()

screen.exitonclick()