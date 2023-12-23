import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(height = 400, width = 500)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle do you think will win the race? Enter a colour from VIBGYOR: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_dist = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle=t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=(y_dist[turtle_index]))
    new_turtle.speed(random.randint(0,10))    
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: #250 -40/2
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!. The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost!. The {winning_color} turtle is the winner!!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


