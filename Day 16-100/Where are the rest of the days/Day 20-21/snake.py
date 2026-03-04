from turtle import Turtle

INIT_POS = [-20, 0, 20]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.up()
            turtle.goto(INIT_POS[i], 0)
            self.snake.append(turtle)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.head.fd(20)