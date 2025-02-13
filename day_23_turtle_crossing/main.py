from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from road import Road
from car import Car
import random
import time

#TODO: implement game speed increase on level up and less clutter of cars.

# Set up the game screen.
screen = Screen()
road = Road()
screen.setup(850, 800)
screen.bgcolor('black')
screen.tracer(0)
scoreboard = Scoreboard()
road.draw_markings()
scoreboard.print_level()


# Create a player.
player = Player()

# Create Car objects and position them on the screen
cars = []
positions = [(395, -280), (395, -200), (395, -120), (395, -40), (395, 40), (395, 120), (395, 200), (395, 280)]

# Set up event listeners.
screen.listen()
screen.onkey(player.move, key="Up")

# Gameplay.
game_is_on = True
counter = 0
sleep_time = 0.001

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    if counter % 20 == 0:
        car = Car()
        car.goto(random.choice(positions))
        cars.append(car)
        for car in cars:
            car.move()
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()
    counter += 1

    # Check if player successfully crossed the road for a level update.
    if player.ycor() > 360:
        scoreboard.update_level()
        player.reset_position()

screen.exitonclick()