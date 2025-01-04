from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)      # SCREEN SIZE (600X600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)    # Turn off automatic animation updating....now will use [screen.update()] KILLING ALL ANIMATION, TO ABSTRACT 3 TURTLE'S ENTRY

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()         # called here so the screen continuously refreshes while game is on....to see the snake moving --> only updates the screen when all the segments have moved forward, gives us an assumption that whole thing is moving in one piece
    time.sleep(0.1)           # The primary purpose of time.sleep() is to halt the execution of the program for a set duration. When used in a game loop, it helps control the speed of game events, such as the movement of objects or checking for collisions.
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()           # Scoreboard reset = 0, ready for next round
        snake.reset()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()       # Scoreboard reset = 0, ready for next round
            snake.reset()
screen.exitonclick()



