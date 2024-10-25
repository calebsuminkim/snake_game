from turtle import Turtle
import random


class Food(Turtle):     # Turtle클래스를 상속
    # TODO: 먹이를 화면에 그림
    # TODO: 먹이와 뱀이 닿을 때마다 임의에 위치에 먹이가 새로 생성됨
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)     # stretch_len = 1(default)은 직경 20x20짜리
        self.color("aquamarine")
        self.speed("fastest")       # 먹이가 새로 생성되는 과정이 보이지 않도록 눈속임
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # -300 ~ 300 좌표평면 위에서 너무 벽에 붙지 않기 위함
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)  # setposition
        print("A new food has been generated.")