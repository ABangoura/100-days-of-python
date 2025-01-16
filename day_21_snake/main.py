from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen.
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('SNAKE!')
screen.tracer(0)

# Create game components
snake = Snake()
food = Food()
score_board = Scoreboard()
score_board.color('white')

# Set up event listeners.
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Game play.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        score_board.update_score()
        snake.add_segment(snake.snake_segments[-1].position())
        food.move()

    #Detect collision with wall.
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        game_is_on = False
        score_board.game_over()

    #Detect collision with tail.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 1:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()