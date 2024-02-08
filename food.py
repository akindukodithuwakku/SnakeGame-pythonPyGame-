
from  turtle import Turtle
import random

class Food(Turtle):

    def __init__( self ):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed("fastest")
        self.color("white")

        self.refresh() #refresh method got from the refreth function

    def refresh( self ):
        randomX = random.randint(-270, 270)
        randomY = random.randint(-270, 270)
        self.goto(randomX,randomY)
