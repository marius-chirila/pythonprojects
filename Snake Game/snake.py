from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)

class Snake: 
    def __init__(self):
        self.x = 0
        self.segments = []
        for i in range (3):
            globals()[f"snake_{i}"] = Turtle("square") 
            globals()[f"snake_{i}"].penup()
            globals()[f"snake_{i}"].color("white")
            globals()[f"snake_{i}"].goto(self.x,0)
            self.x -= 20
            self.segments.append(globals()[f"snake_{i}"])
        screen.update()
   
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)