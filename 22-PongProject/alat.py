from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(270)
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.teleport(x=0, y=300)
        while self.ycor() != -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


class Paddle1(Turtle):

    def __init__(self):
        super().__init__()
        self.resizemode("user")
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.teleport(-380, 0)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


class Paddle2(Paddle1):

    def __init__(self):
        super().__init__()
        self.teleport(380, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.01

    def move(self):
        absis = self.xcor() + self.xmove
        ordi = self.ycor() + self.ymove
        self.goto(absis, ordi)

    def bounce(self, xk, yk):
        self.ymove *= yk
        self.xmove *= xk
        self.move()
        self.move_speed *= 0.9


class Skor2(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(100,200)
        self.hideturtle()
        self.skor = 0

    def board(self):
        self.write(self.skor,align="left" ,font=("Courier", 80, "normal"))

class Skor1(Skor2):
    def __init__(self):
        super().__init__()
        self.goto(-100, 200)

    def board(self):
        super().write(self.skor,align="right" ,font=("Courier", 80, "normal"))