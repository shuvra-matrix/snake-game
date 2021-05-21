from turtle import Turtle

TURTLE_POSITION = [(0, 0), (0, 0), (0, 0)]
SNAKE_MOVE = 8
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.snake_head = self.turtle_list[0]

    def create_snake(self):
        for positions in TURTLE_POSITION:
            self.snake_segment(positions)

    def snake_segment(self, positions):
        tim = Turtle("square")
        tim.shapesize(0.7)
        tim.penup()
        tim.color("white")
        tim.speed("fastest")
        tim.goto(positions)
        self.turtle_list.append(tim)
        self.turtle_list[0].shape("arrow")
        var = self.turtle_list[len(self.turtle_list)-2].color("blue")

    def snake_move(self):
        for ranges in range(len(self.turtle_list) - 1, 0, -1):
            x_position = self.turtle_list[ranges - 1].xcor()
            y_position = self.turtle_list[ranges - 1].ycor()
            self.turtle_list[ranges].goto(x_position, y_position)

        self.snake_head.forward(SNAKE_MOVE)

    def extend_snake(self):
        self.snake_segment(self.turtle_list[-1].position())
        self.turtle_list[0].color("red")
        self.turtle_list[1].color("red")

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def restart_snake(self):
        for turtle in self.turtle_list:
            turtle.goto(1500,1500)

        self.turtle_list.clear()
        self.create_snake()
        self.snake_head = self.turtle_list[0]



