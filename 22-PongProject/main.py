from turtle import Screen
from alat import Net, Paddle1, Paddle2, Skor1, Skor2, Ball
from random import randint
import time

window = Screen()
window.bgcolor("black")
window.title("PingPong Ala-ala")
window.setup(width=800, height=600)
window.listen()
window.tracer(0)

net = Net()
user = Paddle1()
user2 = Paddle2()
skor1 = Skor1()
skor2 = Skor2()
skor1.board()
skor2.board()
ball = Ball()


def start1():
    return randint(-10, -5)


def start2():
    return randint(5, 10)


def acaky():
    x = randint(-10, 10)
    if x != 0:
        return x
    else:
        acaky()


game = True
while game:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce(1, -1)

    if ball.xcor() < -380 and ball.distance(user) < 50:
        ball.bounce(-1, 1)
    if ball.xcor() > 380 and ball.distance(user2) < 50:
        ball.bounce(-1, 1)

    if ball.xcor() <= -400:
        skor2.skor += 1
        ball.home()
        ball.xmove = start2()
        ball.ymove = acaky()
        skor2.clear()
        skor2.board()
        ball.move_speed *= 0.5

    if ball.xcor() >= 400:
        skor1.skor += 1
        ball.home()
        ball.xmove = start1()
        ball.ymove = acaky()
        skor1.clear()
        skor1.board()
        ball.move_speed *= 0.5

    window.onkeypress(user.up, "w")
    window.onkeypress(user.down, "s")
    window.onkeypress(user2.up, "Up")
    window.onkeypress(user2.down, "Down")
    print(ball.move_speed)

    window.update()

window.exitonclick()
