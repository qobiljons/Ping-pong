from turtle import Turtle
UP = 90
DOWN = 270
SPEED = 50


class Player(Turtle):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.setheading(270)
        self.speed(0)
        self.penup()
        self.goto(x, 0)

    def up(self):
        if self.ycor() < 315:
            self.setheading(UP)
            self.forward(SPEED)

    def down(self):
        y = self.ycor()
        if self.ycor() > -315:
            self.sety(y - SPEED)


