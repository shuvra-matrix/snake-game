from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
from bigfood import Bigfood
import time

speed = [0.2, 0.1, 0.04]

screen = Screen()
screen.bgcolor("gray10")
screen.setup(width=600, height=600)
screen.title("Snake Game")
LEVEL = screen.textinput(title="Choose Your Game Level", prompt=" EASY = E , NORMAL = N , HARD = H").lower()
# NAME = screen.textinput(title="Choose Your Game Level", prompt=" Players name").upper()

screen.tracer(0)
screen.listen()

# tim = Turtle()
# tim.penup()
# tim.hideturtle()
# tim.goto(180, 270)
# tim.color("red")
# file = open("name.txt")
#tim.write(f"[ NAME = {file.read()} ", align="center", font=("Comic Sana MS", 12, "bold"))
# file.close()
snake = Snake()
foods = Food()
score = Score()
# score.name(NAME=f"{NAME}")
b_food = Bigfood()
b_food.hideturtle()

screen.onkey(key="W", fun=snake.up)
screen.onkey(key="S", fun=snake.down)
screen.onkey(key="A", fun=snake.left)
screen.onkey(key="D", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_not_finished = True

while is_game_not_finished:
    screen.update()
    if LEVEL == "e":
        time.sleep(speed[0])
    elif LEVEL == "n":
        time.sleep(speed[1])
    elif LEVEL == 'h':
        time.sleep(speed[2])
    snake.snake_move()
    if snake.snake_head.distance(foods) < 15:
        foods.positions()
        snake.extend_snake()
        score.real_score()
    if score.current_score % 20 == 0 and score.current_score != 0:
        b_food.showturtle()

        if snake.snake_head.distance(b_food) < 15:
            b_food.b_positions()
            snake.extend_snake()
            snake.extend_snake()
            snake.extend_snake()
            score.big_food_score()
            b_food.hideturtle()

    if score.current_score % 20 != 0:
        b_food.hideturtle()

    if snake.snake_head.xcor() > 293 or snake.snake_head.xcor() < -293 or snake.snake_head.ycor() > 293 or snake.snake_head.ycor() < -293:
        score.reset_score_again()
        again = screen.textinput(title="Do You Want to Play again",
                                 prompt=" Press R = Play Again\n Press Q = Not Now").lower()
        if again == 'r':
            is_game_not_finished = True
            snake.restart_snake()
            # player_name = screen.textinput(title="player name", prompt=" Enter You Name").lower()
            # if score.current_score > score.high_score:
            #     with open("name.txt", mode="w") as name:
            #         name.write(player_name)
        elif again == 'q':
            is_game_not_finished = False
            score.game_over()

    for head in snake.turtle_list:
        if head == snake.snake_head:
            pass
        elif snake.snake_head.distance(head) < 5:
            score.reset_score_again()
            snake.restart_snake()
screen.exitonclick()
