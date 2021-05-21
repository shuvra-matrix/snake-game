from turtle import Turtle
from random import randint


class Bigfood(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.b_positions()

    def b_positions(self):
        x_position = randint(-280, 280)
        y_position = randint(-280, 280)
        self.goto(x_position, y_position)
