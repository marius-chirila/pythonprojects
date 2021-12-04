from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(1,2,0)
        self.goto(300, random.randint(-240, 250))
        self.seth(180)
        self.move_speed = 5
    
        
    def move_car(self):
        self.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT

       

