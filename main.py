from turtle import  Turtle,Screen
from Timmy import TimmyTurtle
from Cars import Cars
from Scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Welcome to Turtle Road Crossing Game")
screen.tracer(0)

# Setting up Turtle for Crossing:
timmy = TimmyTurtle()
car = Cars()
score = ScoreBoard()
screen.listen()
screen.onkey(fun=timmy.up, key="Up")
car.hideturtle()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.creating_car()
    car.move_cars()
    for i in car.cars:
        if i.distance(timmy) < 30:
           game_on = False
           score.game_over()

    if timmy.ycor() >= 270:
        score.increase_score()
        timmy.start_position()
        car.increase_speed()





screen.exitonclick()