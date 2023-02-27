from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()
    def lose_screen(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over, Final Score: {self.score}", False, align=ALIGN, font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard = {self.score}", False, align=ALIGN, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()