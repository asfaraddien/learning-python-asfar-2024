import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Tutor Nyebrang")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

kura = Player()
cars = CarManager()
scoreboard = Scoreboard()
scoreboard.level_is()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.buat()
    cars.maju(scoreboard.level)

    if kura.xcor() >= 300 or kura.xcor() <= -300:
        kura.setx(-kura.xcor())
    if kura.ycor() <= -300:
        kura.balik()

    for car in cars.cars:
        if kura.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    if kura.ycor() >= 280:
        scoreboard.level += 1
        scoreboard.clear()
        scoreboard.level_is()
        kura.balik()
        if cars.b != 2:
            cars.b -= 1

    screen.onkeypress(kura.up, "Up")
    screen.onkeypress(kura.down, "Down")
    screen.onkeypress(kura.right, "Right")
    screen.onkeypress(kura.left, "Left")
    screen.update()

screen.exitonclick()
