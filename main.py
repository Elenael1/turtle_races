import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=600, height=500)

user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

colors = ["yellow", "red", "orange", "green", "purple", "blue"]
y_position = [0, 50, 100, -50, -100, 150]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 265:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
