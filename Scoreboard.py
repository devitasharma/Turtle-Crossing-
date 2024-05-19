from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-260,280)
        self.write(f"Level={self.score}",align="center",font=("Courier",10,"bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score={self.score}", align="center", font=("Courier", 10, "bold"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courior", 30, "normal"))