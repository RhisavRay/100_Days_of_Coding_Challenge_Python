from turtle import Screen
from snake import Snake
from food import Food
from score_card import ScoreCard

screen = Screen()
screen.setup(width=600, height=600)
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

game_is_on = True

def game_loop():
    global game_is_on
    if game_is_on:
        snake.move()
        if food.collision_detection(snake.head):
            score_card.gain_score()
            print(score_card.score)
        screen.update()
        screen.ontimer(game_loop, 100)


# TODO 6: Make the snake grow upon eating the food



# TODO 7: Add score feature



# TODO 8: Add the GAME OVER logic (Hitting wall or biting own tail)

game_loop()

screen.exitonclick()