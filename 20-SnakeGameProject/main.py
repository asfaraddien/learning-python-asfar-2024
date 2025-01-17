from turtle import Turtle, Screen
from food import Food
from snake import Snake
from score import Score
import time

# snake = Turtle()
# snake.penup()
# snake.resizemode("user")
# snake.shapesize(stretch_len=3)
# snake.color("white")
# snake.shape("square")
# snake.shapesize()

window = Screen()
window.setup(width=600, height=600)
window.title("Nostalgia Game Ular")
window.bgcolor("black")
window.listen()
window.tracer(0)

skor = Score()
ular = Snake()
makan = Food()


window.onkey(ular.up, "Up")
window.onkey(ular.down, "Down")
window.onkey(ular.left, "Left")
window.onkey(ular.right, "Right")

game = True
while game:
    window.update()
    time.sleep(0.1)
    ular.formasi()

    if ular.segment[0].distance(makan) < 15:
        makan.pindah()
        skor.skor += 1
        skor.muncul()
        ular.ekor_baru_di()


    if ular.segment[0].xcor() > 280:
        new1 = (-280, ular.segment[0].ycor())
        ular.segment[0].goto(new1)

    elif ular.segment[0].ycor() > 280:
        new2 = (ular.segment[0].xcor(), -280)
        ular.segment[0].goto(new2)

    elif ular.segment[0].ycor() < -280:
        new3 = (ular.segment[0].xcor(), 280)
        ular.segment[0].goto(new3)

    elif ular.segment[0].xcor() < -280:
        new1 = (280, ular.segment[0].ycor())
        ular.segment[0].goto(new1)


    # Mati kalo kena tail
    for segmen in ular.segment[1:]:
        if ular.segment[0].distance(segmen) < 10:
            skor.high()
            ular.ulang()




        #if ular.segment.index(segmen) != 0 and segmen.position() == ular.segment[0].position():
        # if ular.segment.index(segmen) == 0:
        #     pass




window.exitonclick()
