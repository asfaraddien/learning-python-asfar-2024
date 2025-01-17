from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.skor = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Skor kamu: {self.skor}     High score: {self.high_score}", align="center", font=("Arial", 15, "normal"))

    def high(self):
        if self.skor > self.high_score:
            self.high_score = self.skor
            with open("data.txt", mode="w") as baru:
                baru.write(str(skor.high_score))
        self.skor = 0
        self.muncul()


    def muncul(self):
        self.clear()
        self.write(f"Skor kamu: {self.skor}     High score: {self.high_score}", align="center", font=("Arial", 15, "normal"))





    # def mati(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
