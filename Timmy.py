from turtle import Turtle, Screen

class TimmyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.start_position()


    def up(self):
        self.forward(30)

    def start_position(self):
        self.goto(0, -280)
