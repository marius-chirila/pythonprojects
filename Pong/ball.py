from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movespeed = 15

    def move_ball(self, bounce):
        self.seth(bounce)
        self.forward(self.movespeed)

    def move_ball_x(self):
        self.seth()
        
       
        
            
        