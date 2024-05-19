from turtle import *
import turtle
import random



class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.move = 10
        self.color_list = ["red", "green", "yellow", "blue", "pink", "orange", "brown","purple","grey","pink",
                           "yellow","red", "green", "yellow", "blue"]
        self.cars = []
        self.creating_car()



    def creating_car(self):
        random_car_generate=random.randint(1,5)
        if random_car_generate == 1:
                car = Turtle("square")
                car.shapesize(1, 2)
                car.setheading(180)
                car.color(random.choice(self.color_list))
                car.penup()
                car.goto(260, random.randint(-250, 250))
                self.cars.append(car)




    def move_cars(self):
        for i in self.cars:
            i.forward(self.move)


    def increase_speed(self):
       self.move += 10


























