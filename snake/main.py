import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
game_over=False
food = Food()
snake = Snake()
scoreboard = Scoreboard()
Screen().listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<20:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
    if snake.head.xcor()>=280 or snake.head.xcor()<=-280 or snake.head.ycor()>=280 or snake.head.ycor()<=-280:
        game_over=True
        scoreboard.lose_screen()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:

            game_over=True
            scoreboard.lose_screen()



























screen.exitonclick()