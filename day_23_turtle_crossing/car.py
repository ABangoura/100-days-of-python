from turtle import Turtle
import random

class Car(Turtle):
    """ Car class represented by rectangles. """
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.new_color()
        self.penup()
        self.shapesize(1.5, 3, 1)
        self.setheading(180)
        self.move_distance = 10

    def move(self):
        """ Method to move the car forward. """
        self.forward(self.move_distance)

    def new_color(self):
        """ Method to choose a new car color. """
        colors = ['red', 'blue', 'yellow', 'green','gold', 'lime', 'white', 'magenta' ]
        self.color(random.choice(colors))

    def level_up(self):
        """ Method to increase the speed of the cars by increasing the distance covered. """
        self.move_distance += 10