import turtle
import pandas

window = turtle.Screen()
window.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

skor = 0
benar = []
salah = []
game = True
while game:
    tebakan = window.textinput(title=f"Tebak Negeri {skor}/50 ", prompt="tebak!").title()
    data = pandas.read_csv("50_states.csv")
    negeri = data.state
    negeri_list = negeri.to_list()

    if tebakan == "Exit":
        break
    if tebakan in negeri_list and tebakan not in benar:
        jawaban = data[negeri == tebakan]
        x = int(jawaban.x.iloc[0])
        y = int(jawaban.y.iloc[0])
        cord = (x, y)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(cord)
        t.write(tebakan)
        benar.append(tebakan)
        skor += 1
    else:
        salah.append(tebakan)

salahcsv = pandas.DataFrame(salah)
salahcsv.to_csv("salah.csv")


window.exitonclick()