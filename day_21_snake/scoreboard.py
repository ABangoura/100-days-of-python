from turtle import Turtle

class Scoreboard(Turtle):
    """ Class to represent the scoreboard. """
    def __init__(self):
        """ Initialization method. """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 370)
        self.score = 0
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def update_score(self):
        """ Method to update the score. """
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        """ Method to announce GAME OVER! """
        # Go to center of screen then write GAME OVER!
        self.goto(0, 0)
        self.write('GAME OVER!', align='center' , font=('Arial', 24, 'normal'))