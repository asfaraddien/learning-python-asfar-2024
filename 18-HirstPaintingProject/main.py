###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle

import colorgram
from turtle import Turtle, Screen, colormode

turtle.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
dots = Turtle()

dots.penup()
dots.speed("fastest")
dots.hideturtle()

dots.setheading(225)
dots.forward(500)
dots.left(135)
for i in range(10):
    for y in range(10):
        dots.dot(20, random.choice(colors))
        dots.forward(50)
    if i != 9:
        dots.back(500)
        dots.left(90)
        dots.forward(50)
        dots.right(90)





window = Screen()
window.exitonclick()