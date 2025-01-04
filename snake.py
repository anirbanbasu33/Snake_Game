from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]         # setting global constants, accessed from anywhere
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()                 # This triggers whenever the snake object is called at main.py
        self.head = self.segments[0]        # Positioning of code is extremely important
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Actually adding all turtle segments here based on the provided position
        tim = Turtle(shape='square')
        tim.color('white')
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)     # get the snake out of present screen, make room for new snake
        self.segments.clear()   # all snake body segments are deleted
        self.create_snake()     # INITIALISING THE SNAKE AGAIN...new snake created at starting position for new game
        self.head = self.segments[0]
    def extend(self):
        # Add a new segment everytime it eats food at the last segment's position... segments[-1]
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:      # Avoiding collision
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)



