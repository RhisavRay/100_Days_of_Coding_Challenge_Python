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

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.head.fd(20)

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

    @staticmethod
    def create_segment(position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        return new_segment

    def grow_snake(self):
        new_position = self.snake[-1].pos()
        new_segment = self.create_segment(new_position)
        self.snake.append(new_segment)

    def wall_collision(self):
        if abs(self.head.xcor()) > 300 or abs(self.head.ycor()) > 300:
            return True
        return False