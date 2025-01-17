from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.speed(0)
        self.goto(STARTING_POSITION)

    def up(self):
        ordin = self.ycor() + MOVE_DISTANCE
        self.sety(ordin)
    def down(self):
        ordin = self.ycor() - MOVE_DISTANCE
        self.sety(ordin)

    def right(self):
        absis = self.xcor() + MOVE_DISTANCE
        self.setx(absis)

    def left(self):
        absis = self.xcor() - MOVE_DISTANCE
        self.setx(absis)

    def balik(self):
        self.goto(STARTING_POSITION)
