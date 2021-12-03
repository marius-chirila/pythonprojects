from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.onkeypress(paddle.move_paddle_up, "Up")
screen.onkeypress(paddle2.move_paddle_up, "w")
screen.onkeypress(paddle.move_paddle_down, "Down")
screen.onkeypress(paddle2.move_paddle_down, "s")
position = random.randint(1, 359)

game_is_on = True
#main game loop
while game_is_on:
   
    screen.update()
    time.sleep(0.04)
    #checking collision with walls
    if ball.ycor() > 285 or ball.ycor() < -280:
        position = 360 - (ball.heading())
        ball.move_ball(position)
    #checking collision with paddles
    elif (ball.distance(paddle) < 50 and ball.xcor() > 320 and ball.xcor() < 380) or (ball.distance(paddle2) < 50 and ball.xcor() < -320 and ball.xcor() > - 380):
        position = 360 - 180 - (ball.heading())
        ball.movespeed += 2
        ball.move_ball(position)
    elif (ball.xcor() > 400):
        score.point_p1()
        ball.home()
        position = random.randint(110, 250)
        ball.movespeed = 15
    elif (ball.xcor() < -400):
        score.point_p2()
        ball.home()
        choice = []
        choice.append(random.randint(20,70)) 
        choice.append(random.randint(270, 340))
        position = random.choice(choice)
        ball.movespeed = 15 
    else:
        ball.move_ball(position)    
    
    

screen.exitonclick()