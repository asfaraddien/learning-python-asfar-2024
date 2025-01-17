from turtle import Turtle, Screen
import random

window = Screen()
window.setup(width=700, height=400)
colors = ["black", "magenta", "green", "blue", "red", "purple"]
turtles = []
pilihan = window.textinput("Balap Kura", "Pilih warna kura!: ")


for i in range(0, 6):
    timmy = Turtle()
    timmy.speed("fastest")
    timmy.color(colors[i])
    timmy.shape("turtle")
    timmy.penup()
    i *= 50
    timmy.goto(x=-330, y=-140 + i)
    turtles.append(timmy)

game = True
while game:
    for peserta in turtles:
        if peserta.xcor() > 330:
            game = False
            if peserta.pencolor() == pilihan:
                print(f"Kamu menang, {pilihan} menang.")
            elif peserta.pencolor() != pilihan:
                print(f"Kamu kalah, {peserta.pencolor()} menang.")
    for peserta in turtles:
        peserta.forward(random.randint(0, 10))











window.exitonclick()




# def maju():
#     timmy.forward(10)
#
#
# def mundur():
#     timmy.back(10)
#
#
# def clockwise():
#     new = timmy.heading() - 10
#     timmy.setheading(new)
#
#
# def anticlock():
#     new = timmy.heading() + 10
#     timmy.setheading(new)
#
#
# window.listen()
# window.onkey(key="w", fun=maju)
# window.onkey(key="a", fun=anticlock)
# window.onkey(key="s", fun=mundur)
# window.onkey(key="d", fun=clockwise)
