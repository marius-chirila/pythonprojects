from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)

#creates snake
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#moving snake - block/by/block
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    
        


screen.exitonclick()
