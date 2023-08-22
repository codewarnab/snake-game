# Import necessary modules and classes
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Disable automatic screen update

# Create instances of Snake, Food, and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up key listeners for snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Enable manual screen updates
    time.sleep(0.12)  # Introduce a delay between each iteration
    snake.move()  # Move the snake

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()  # Generate a new food item
        snake.extend()  # Extend the snake's length
        scoreboard.increase_score()  # Update the score displayed

    # Detect collision with wall.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()  # Reset the score
        snake.reset()  # Reset the snake's position and length
        scoreboard.update_scoreboard()  # Update the score display

    # Detect collision with tail.
    for segment in snake.segments[1:]:  # Check collision with each segment of the snake's tail
        if snake.head.distance(segment) < 10:
            scoreboard.reset()  # Reset the score
            snake.reset()  # Reset the snake's position and length
            scoreboard.update_scoreboard()  # Update the score display

# Close the game when clicked
screen.exitonclick()
