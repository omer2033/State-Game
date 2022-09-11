# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
new_turtle = turtle.Turtle()
new_turtle.hideturtle()

## Iterating data from 50 states
data = pandas.read_csv("50_states.csv")
states = data.state
x_cordinate = data.x
y_cordinate = data.y
states_correct = []
len_question = 0
user_score = 0
states_for_learning = []

def write_on_screen(a):
    """To Write Correct State On Screen"""
    horizantal = data[data.state == state].x
    vertical = data[data.state == state].y
    new_turtle.penup()
    new_turtle.goto(int(horizantal),int(vertical))
    new_turtle.write(state)


while len_question <=50:
    ## main part of the program
    answer_state = screen.textinput(title=f"{len_question}/50 Guess the State", prompt="What's another state's name?")
    len_question += 1
    answer_state.lower()
    if answer_state == "exit":
        break
    for state in states:
        if state.lower() == answer_state:
            states_correct.append(state)
            write_on_screen(state)
            user_score += 1


new_data = pandas.DataFrame(states_for_learning)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()









