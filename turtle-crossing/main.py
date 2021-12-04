import time
from turtle import Screen
from player import *
from car_manager import *
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkeypress(player.move_turtle, "Up")
screen.title("Turtle road cross")

cars = []
cars_speed = STARTING_MOVE_DISTANCE
    
game_is_on = True
while game_is_on:  
    time.sleep(0.1)
    screen.update()
    
    if player.ycor() >= FINISH_LINE_Y:
        player.goto(0, -280)        
        scoreboard.update_score()
        for i in cars:
            i.move_speed += MOVE_INCREMENT
        cars_speed += MOVE_INCREMENT

    random_chance = random.randint(1,5)
    if random_chance == 1:
                car = CarManager()
                car.move_speed = cars_speed
                cars.append(car)

    for i in cars:
        i.move_car()
        if player.distance(i) < 23:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()