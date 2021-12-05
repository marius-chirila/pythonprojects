from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)

#creates snake
snake = Snake()
#creates food
food = Food()
score = Scoreboard()

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
    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score()
        snake.add_segments()
    #detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    #detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()
        
        


screen.exitonclick()
