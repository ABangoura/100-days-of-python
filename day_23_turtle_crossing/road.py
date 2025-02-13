from turtle import Turtle

class Road(Turtle):
    """ Road class """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(5)
        self.pencolor('white')
        self.penup()
        self.setheading(180)
        self.x_position = 400
        self.y_position = -320
        self.DASH = 40
        self.SPACE = 20
        self.goto(self.x_position, self.y_position)

    def draw_markings(self):
        """ Method to draw the white markings on the road"""
        for _ in range(0, 2520, 20):
            if self.xcor() <= -425:
                self.y_position += 80
                self.goto(self.x_position, self.y_position)

            self.pendown()
            self.forward(self.DASH)
            self.penup()
            self.forward(self.SPACE)