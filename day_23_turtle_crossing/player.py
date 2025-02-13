from turtle import Turtle

class Player(Turtle):
    """ Player class represented by the turtle character. """
    def __init__(self):
        super().__init__()
        self.speed(10)
        self.shapesize(1.3, 1.3, 1)
        self.steps = 10
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(0, -360)

    def move(self):
        """ Method to move the turtle one step forward. """
        self.forward(self.steps)

    def reset_position(self):
        """ Method to take the player back to the bottom of the screen for another crossing attempt. """
        self.goto(0, -360)