""""
how to import module?

1] import {module}
2] from {module} import {thing}
3] from {module} import * (semua yang ada didalam)
4] import {module: turtle} as t (disingkat)

"""
import turtle

import heroes
from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
turtle.colormode(255)

def warna():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    return (r, g, b)


# i = 0
# while i != 4:
#     for x in range(15):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()
#     timmy.right(90)
#     i += 1


# color = ["blue", "red", "cyan", "yellow", "green", "purple", "magenta", "orange"]
# for i in range(3, 11):
#     for x in range(i):
#         timmy.pencolor(color[i - 3])
#         timmy.forward(100)
#         timmy.right(360/i)

# color = ["blue", "red", "cyan", "yellow", "green", "purple", "magenta", "orange"]
# def acak(a, b):
#     return random.randint(a, b)
#
# for i in range(acak(1, 50)):
#     random.choice(color)
#     timmy.forward(acak(1, 100))
#     timmy.left(acak(1, 360))
#     timmy.forward(acak(1, 100))
#     timmy.left(acak(1, 360))

# timmy.pensize(15)
# timmy.speed(0)
# for _ in range(200):
#     timmy.pencolor(warna())
#     timmy.forward(20)
#     timmy.setheading(random.choice([0, 180, 90, 270]))


timmy.speed(0)
gap = 10
for _ in range(int(360/gap)):
    timmy.pencolor(warna())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + gap)
    print(timmy.heading())





window = Screen()
window.exitonclick()
