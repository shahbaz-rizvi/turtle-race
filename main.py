from turtle import Turtle, Screen
import random

is_race_active = False
screen = Screen()
screen.setup(width=500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postiions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postiions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_active = True
while is_race_active:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_active = False
            winning_color = turtle.pencolor()
            if winning_color ==user_bet:
                print ("You won!")
            else:
                print(f"You lost! the winner is {winning_color} turtle")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
