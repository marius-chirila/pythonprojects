from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")

x = 0
for i in range (3):
    globals()[f"snake_{i}"] = Turtle("square") 
    globals()[f"snake_{i}"].penup()
    globals()[f"snake_{i}"].color("white")
    globals()[f"snake_{i}"].goto(x,0)
    x -= 20
screen.exitonclick()
