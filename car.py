from turtle import Turtle
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('green')
        self.move()

    def move(self):
        self.forward(2)