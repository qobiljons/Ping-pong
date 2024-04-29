from turtle import Turtle

FONT = ("Courier", 56, "normal")


class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.text = None
        self.penup()
        self.speed(0)
        self.goto(0, 320)
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        text = f"{self.l_score}:{self.r_score}"
        self.write(text, align="center", font=FONT)

    def increase_l(self):
        self.clear()
        self.l_score += 1
        self.update()

    def increase_r(self):
        self.clear()
        self.r_score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        if self.l_score > 1:
            self.text = "The Opponent wins"
        elif self.r_score > 1:
            self.text = "The Player wins"
        self.write(self.text, align="Center", font=FONT)


