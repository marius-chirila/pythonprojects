from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./Snake Game/data.txt", "r") as file:
            self.highscore = int(file.read())
        self.goto(0, 280)
        self.penup()
        self.color("white")
        self.write(f"Current score is: {self.score}, Highscore: {self.highscore}", False, align="center", font=("Calibri", 15, "bold"))
        self.ht()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Current score is: {self.score}, Highscore: {self.highscore}", False, align="center", font=("Calibri", 15, "bold"))
    
  # def game_over(self):
  #      self.goto(0, 0)
  #      self.write(f"Game over", align="center", font=("Calibri", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            with open("./Snake Game/data.txt", "w") as file:
                file.write(str(self.score))
            with open("./Snake Game/data.txt", "r") as file:
                self.highscore = int(file.read())   
        self.score = 0
        self.clear()
        self.write(f"Current score is: {self.score}, Highscore: {self.highscore}", False, align="center", font=("Calibri", 15, "bold"))