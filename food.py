from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red3")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.positions()

    def positions(self):
        x_position = randint(-280, 280)
        y_position = randint(-280, 280)
        self.goto(x_position, y_position)


