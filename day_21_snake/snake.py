from turtle import Turtle
import random

class Snake:
    """ Snake class. """
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0
    MOVE_DISTANCE = 20
    colors = ['white', 'red', 'yellow', 'green', 'blue', 'orange', 'orchid', 'lime']

    def __init__(self):
        """ Initialization method. """
        self.snake_segments = []
        # Initialize the snake with the first 3 segments,
        # and their initial positions.
        for position in range(3):
            self.add_segment((position * -20, 0))
            self.head = self.snake_segments[0]

    def move(self):
        """ Method to move the different segments of the snake. """
        # Starting from the ending segment, move the snake forward.
        for segment_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_number - 1].xcor()
            new_y = self.snake_segments[segment_number - 1].ycor()
            self.snake_segments[segment_number].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        """ Method to move the snake upward. """
        # Move the snake UP only if it's not headed DOWN
        # to avoid running into itself.
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        """ Method to move the snake downward. """
        # Move the snake DOWN only if it's not headed UP
        # to avoid running into itself.
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        """ Method to move the snake left. """
        # Move the snake LEFT only if it's not headed RIGHT
        # to avoid running into itself.
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        """ Method to move the snake right. """
        # Move the snake RIGHT only if it's not headed LEFT
        # to avoid running into itself.
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def add_segment(self, position):
        """ Method to add a new segment to the snake. Takes the position
        coordinates as a tuple parameter. """
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color(random.choice(self.colors))
        new_segment.goto(position)
        self.snake_segments.append(new_segment)