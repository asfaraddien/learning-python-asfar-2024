from turtle import Turtle

LETAK = [(0, 0), (-20, 0), (-40, 0)]
speed = 20


class Snake:

    def __init__(self):
        self.segment = []
        self.buattail()

    def buattail(self):
        for seg in LETAK:
            self.nambah_ekor(seg)

    def nambah_ekor(self, seg):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(seg)
        self.segment.append(segment)

    def ekor_baru_di(self):
        cord = (self.segment[-1].position())
        self.nambah_ekor(cord)

    def ulang(self):
        for i in self.segment:
            i.setx(1000)
        self.segment.clear()
        self.buattail()


    def formasi(self):
        for i in range(len(self.segment) - 1, 0, -1):
            absis = self.segment[i - 1].xcor()
            ordin = self.segment[i - 1].ycor()
            self.segment[i].goto(absis, ordin)
        self.segment[0].forward(speed)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)


