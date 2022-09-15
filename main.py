"""
Project name - Turtle racing
Author - Dheeraj Kumar
"""
from turtle import Turtle, Screen   # pip install turtle
import random   # built in module

is_race_on = False

# screen setup
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a code: ") # user choice
colors = ["red", "blue", "yellow", "purple", "green", "orange"]  # turtle colors
y_position = [-70, -40, -10, 20, 50, 80] # position of turtle in field
all_turtle = []
for turtle_index in range(0, 6):
    # turtle setup and size
    dj = Turtle(shape = "turtle")
    dj.color(colors[turtle_index])
    dj.penup()
    dj.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(dj)

# conditions
if user_bet:
    is_race_on = True # condition is true then turtle are run
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:  # final condition winner/runner
                print(f"You've won! {winning_color} turtle is winner!")
            else:
                print(f"You've lost! {winning_color} turtle is winner!")

        rand_distance = random.randint(0, 10)  # use random module
        turtle.forward(rand_distance)  # turtle randomly forwarded
screen.exitonclick()  #  for when user wants to exit the game