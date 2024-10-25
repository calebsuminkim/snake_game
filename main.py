from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("coral")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:  #먹이의 직경이 10x10짜리임을 감안하여, 여유공간 포함한 거리
        food.refresh()
        scoreboard.record_the_score()   # 점수를 다시 씀
        snake.extend() # 먹이 먹으면 하나 늘어남

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with its tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # A.distance(B) : 객체 A와 객체 B사이의 거리를 리턴
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()