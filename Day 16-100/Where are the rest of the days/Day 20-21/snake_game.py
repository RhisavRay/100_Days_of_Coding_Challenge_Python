from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

# TODO 4: Make food dots in random location on the screen



# TODO 5: Upon eating the food, another food dot appears at random on the screen



# TODO 6: Make the snake grow upon eating the food



# TODO 7: Add score feature



# TODO 8: Add the GAME OVER logic (Hitting wall or biting own tail)



screen.exitonclick()