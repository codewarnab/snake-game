from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []  # List to hold the segments of the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The head of the snake is the first segment

    def create_snake(self):
        '''Create the initial snake with segments.'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        '''Add a new segment to the snake.'''
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        '''Reset the snake to its initial state.'''
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments off-screen
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Update the head reference

    def extend(self):
        '''Extend the snake by adding a new segment.'''
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''Move the snake by updating each segment's position.'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        '''Change the snake's direction to up, unless it's already moving down.'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Change the snake's direction to down, unless it's already moving up.'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Change the snake's direction to left, unless it's already moving right.'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Change the snake's direction to right, unless it's already moving left.'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
