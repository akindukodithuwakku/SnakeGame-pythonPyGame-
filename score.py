
from turtle import Turtle

class Score(Turtle):

    def __init__( self ):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0 , 270)
        self.highscore = 0
        self.update_score_board()
        self.hideturtle()

    def update_score_board( self ):
        self.clear()
        self.write(f"Score:{self.score}: High Score: {self.highscore}" , align="center" , font=("Arial" , 20 , "normal")) # dont use hard coded parts inside the paranthesis
# use constants to build these type of hard coded parts

    def reset( self ):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score_board()

    def increase_score( self ):
        self.score += 1
        self.update_score_board()

    # def game_over( self ):
    #     self.goto(0,0)
    #     self.write(f"Game Over! Your Score:{self.score}" , align="center" , font=("Arial" , 20 , "normal"))
