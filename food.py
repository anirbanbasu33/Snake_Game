# Food class will know how to render itself like a small circle at screen
# Everytime snake hits the food, food reappears at a new random location
# Food will be a turtle object
# As soon as you create a food object at main.py, the enitre __init__ method will be executed

from turtle import Turtle
import random

class Food(Turtle):     # (should have used- self.food = Turtle() inside init, if I dont inherit Turtle class) But here let Food class inherit Turtle class to attain all its attributes ++ some unique features of its own

    def __init__(self):

        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)      # Normally turtle is 20*20 pixels (we are going to halve its size ---(Both dimensions 20*0.5 = 10 x 10 format)
        self.color('blue')
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
