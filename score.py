from turtle import Turtle

with open("h_score.txt", mode="r") as file:
    a = int(file.read())

ALIGNMENT = "center"
FONT = ("Comic Sana MS", 12, "bold")
GAME_FONT = ("Comic Sana MS", 20, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = a
        self.color("turquoise3")
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.goto(-150, 270)
        self.reset_score()

    def reset_score(self):
        self.write(f"[ SCORE = {self.current_score} ]   [HIGH SCORE=  {self.high_score} ] ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("green3")
        self.write(f"GAME OVER ", align=ALIGNMENT, font=GAME_FONT)

    def real_score(self):
        self.current_score += 1
        self.clear()
        self.reset_score()

    def big_food_score(self):
        self.current_score += 5
        self.clear()
        self.reset_score()

    def reset_score_again(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("h_score.txt", mode="w") as files:
                files.write(f"{self.high_score}")
        self.current_score = 0
        self.clear()
        self.reset_score()

    # def name(self, NAME):
    #     if self.current_score > self.high_score or self.current_score == self.high_score:
    #         with open("name.txt",mode="w" ) as name:
    #             name.write(NAME)

