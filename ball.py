from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(1)
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.SPEED = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move()

    def paddle_bounce(self):
        self.x_move *= -1
        self.move()
        self.SPEED *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.paddle_bounce()
