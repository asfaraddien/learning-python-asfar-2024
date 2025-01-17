from turtle import Turtle
from random import randint, choice



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.b = 4

    def buat(self):
        ran = randint(1, self.b)
        if ran == 1:
            car = Turtle("square")
            car.penup()
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.goto(320, randint(-240, 240))
            self.cars.append(car)

    def maju(self, level):
        nambah = level*MOVE_INCREMENT
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + nambah)

        # for i in range(6):
        #     mobil = self.cars[randint(0, 5)]
        #     mobil.forward(30)
        #     if mobil.xcor() <= 320:
        #         mobil.goto(320, 0)







