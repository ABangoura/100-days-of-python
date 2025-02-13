from turtle import Turtle

class Scoreboard(Turtle):
    """ Class representing the scoreboard. """
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.pensize(5)
        self.pencolor('white')
        self.level = 1

    def print_level(self):
        """ Method to print the game level. """
        self.penup()
        self.goto(-340, 340)
        self.pendown()
        self.write(f'Level:{self.level}', align='center', font=('Courier', 30, 'normal'))

    def update_level(self):
        """ Method to update the game level. """
        self.clear()
        self.level += 1
        self.print_level()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=('Courier', 30, 'normal'))