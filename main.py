""" this game has multiple parts

---------------------------------------
1st we are going to create snake body
2 - move the snake
--------------------------------------

3- create snake foods
4- detect collision with the food
5 - create score board
6- detect collision on walls
7- detect collision with the tail


"""

# author has used the turtle graphic library to implement this solution

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

'''screen related codes here'''
screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.tracer(0)

'''snake object here'''
snake = Snake()  # gnereate a new snake object

'''food object here'''
food = Food()  # generate a new food object

'''score board object here'''
score = Score()

'''screen functionality in here'''
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")


def game():
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)  # Adjust the speed of the snake
        snake.move()  # moving the snake using snake method

        if snake.head.distance(food) < 18:
            food.refresh()
            snake.extend()
            score.increase_score()

        if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
            score.reset()
            snake.reset()

        for segments in snake.all_turtles[1:]:  # data slicing using list slice list[1:] code run without first element
            if snake.head.distance(segments) < 10:
               score.reset()
               snake.reset()


game()

screen.exitonclick()
