from turtle import Turtle

POSITIONS = [(0 , 0) , (-20 , 0) , (-40 , 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__( self ):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake( self ):
        for pos in POSITIONS:
            self.segments(pos)

    def segments( self , pos ):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.all_turtles.append(new_turtle)

    def reset( self ):

        for snake in self.all_turtles:
            snake.goto(1000,1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def extend( self ):
        self.segments(self.all_turtles[-1].pos())

    def move( self ):
        for seg_num in range(len(self.all_turtles) - 1 , 0 , -1):
            new_x = self.all_turtles[seg_num - 1].xcor()
            new_y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(new_x , new_y)

        self.head.forward(MOVE_DIS)  # Move the head forward

    def up( self ):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down( self ):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left( self ):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right( self ):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
