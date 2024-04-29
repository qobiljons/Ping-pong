from turtle import Screen
from player import Player
import time
from ball import Ball
from scoreboard import Pen
GAME = True
pen = Pen()

# Screen Method

screen = Screen()
screen.tracer(0)
screen.bgcolor("lime")
screen.setup(height=800, width=1400)
screen.title("Pong")

# Gamer and the opponent
ball = Ball()
gamer = Player(-660)
opponent = Player(660)

screen.listen()

SLEEP = 0.1
screen.onkeypress(gamer.up, "w")
screen.onkeypress(gamer.down, "s")
screen.onkeypress(opponent.up, "Up")
screen.onkeypress(opponent.down, "Down")

while GAME:
    print(SLEEP)
    screen.update()
    ball.move()
    time.sleep(ball.SPEED)
    if ball.ycor() > 370 or ball.ycor() < - 370:
        ball.bounce()
    if ball.distance(opponent) < 100 and ball.xcor() > 620 or ball.distance(gamer) < 100 and ball.xcor() < -620:
        ball.paddle_bounce()
    elif ball.xcor() > 720:
        ball.reset_ball()
        pen.increase_l()
    elif ball.xcor() < -720:
        ball.reset_ball()
        pen.increase_r()
screen.exitonclick()
