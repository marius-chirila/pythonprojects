from turtle import Turtle, position

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 5, 0)
        self.color("white")
        self.goto(position)
        self.seth(90)
    
    def move_paddle_up(self):
        self.seth(90)
        self.forward(20)

    def move_paddle_down(self):
        self.seth(270)
        self.forward(20)
