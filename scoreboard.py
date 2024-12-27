from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(-20, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", 'r') as file:
            self.high_score = int(file.read())
            print(self.high_score)
            print(f"self.high_score type : {type(self.high_score)}")

        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

