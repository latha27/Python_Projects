from turtle import *
x=0
y=-100

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x, y)
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(x, y)
        self.bounce_y()




