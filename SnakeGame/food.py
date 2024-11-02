from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("DarkMagenta")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_val = random.randint(-280, 280)
        y_val = random.randint(-280, 280)
        self.goto(x_val, y_val)