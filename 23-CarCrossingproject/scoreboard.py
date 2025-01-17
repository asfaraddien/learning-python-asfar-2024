from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)

    def level_is(self):
        self.write(f"level: {self.level}", font=FONT)
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
