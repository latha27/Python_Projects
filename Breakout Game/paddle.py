from turtle import *


MOVE_DIST = 30
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=12)
        self.penup()
        self.goto(position)

    def go_right(self):
        self.forward(MOVE_DIST)

    def go_left(self):
        self.backward(MOVE_DIST)