from turtle import Turtle

CO_ORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in CO_ORDS:
            self.append_seg(i)

    def append_seg(self, pos):
        new_pix = Turtle(shape="square")
        new_pix.color("thistle4")
        new_pix.penup()
        new_pix.goto(pos)
        self.segments.append(new_pix)

    def extend(self):
        self.append_seg(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) -1, 0, -1):
            x_value = self.segments[i - 1].xcor()
            y_value = self.segments[i - 1].ycor()
            self.segments[i].goto(x_value, y_value)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
