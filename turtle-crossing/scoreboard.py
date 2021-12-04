from turtle import Turtle, home
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-290,260)
        self.ht()
        self.level = 1
        self.write(f"Level: {self.level}", False, font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"Game over",  align="center", move=False, font=FONT)
