from turtle import Turtle
from random import randint

class Food:
    def __init__(self):
        self.food_kernel = None
        self.create_food()

    def create_food(self):
        self.food_kernel = Turtle()
        self.food_kernel.color("Green")
        self.food_kernel.shape("circle")
        self.food_kernel.shapesize(0.5, 0.5)
        self.food_kernel.up()
        self.place_food()

    def place_food(self):
        x = randint(-14, 14) * 20  # snaps to grid: -300, -280, ... 280, 300
        y = randint(-14, 14) * 20
        self.food_kernel.goto(x, y)

    def collision_detection(self, snake_head):
        # turtle's xcor()/ycor() return floats with hidden precision drift, e.g. 60 might be stored as 59.9999999999 or 60.0000000001
        # round() ensures these snap to the nearest whole number for reliable comparison
        # int() was tried but it truncates instead of rounding, so 59.999 becomes 59 instead of 60
        head_x, head_y = round(snake_head.xcor()), round(snake_head.ycor())
        food_x, food_y = round(self.food_kernel.xcor()), round(self.food_kernel.ycor())

        # comparing xcor/ycor individually as rounded ints instead of pos() tuples
        # because pos() returns a Vec2D object whose == comparison is unreliable
        if head_x == food_x and head_y == food_y:
            self.place_food()
            return True
        return False