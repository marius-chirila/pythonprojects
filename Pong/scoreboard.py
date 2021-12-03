from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1=0
        self.player2=0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1, False, "center", ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player2, False, "center", ("Courier", 80, "normal"))

    def point_p1(self):
        self.player1 += 1
        self.update_score()


    def point_p2(self):
        self.player2 += 1 
        self.update_score()   