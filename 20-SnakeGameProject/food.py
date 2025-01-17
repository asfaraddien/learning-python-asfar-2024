from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.penup()
        self.color("green")
        self.pindah()

    def pindah(self):
        AXIS = (randint(-280, 280), randint(-280, 260))
        self.goto(AXIS)
