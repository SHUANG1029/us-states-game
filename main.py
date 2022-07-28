import turtle
import pandas

states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()

screen = turtle.Screen()
screen.title("U.S GAME")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
guess_record=[]


while len(guess_record)<50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guess_record:
                missing_states.append(state)
                s_list = pandas.DataFrame(missing_states)
                s_list.to_csv("missing states.csv")
        break
    if answer_state in states_list:
        x1 = int(states[states.state == answer_state]["x"])
        y1 = int(states[states.state == answer_state]["y"])
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x1, y1)
        t.color("black")
        t.write(f"{answer_state}", align="center", font=("Courier", 10, "normal"))
        score += 1
        guess_record.append(answer_state)

    else:
        pass


