import pandas
import turtle

from state_text import StateText

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "./Day 25/us_states/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("./Day 25/us_states/50_states.csv")
state_names = states_data.state.to_list()
state_positions_x = states_data.x.to_list()
state_positions_y = states_data.y.to_list()

correct_guess_total = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title=f"Guess the State {correct_guess_total}/50",
        prompt="What's another states name?",
    ).title()

    if answer_state in state_names:
        correct_guess_total += 1
        state_index = state_names.index(answer_state)
        state_guess = StateText()
        state_guess.write_state(
            f"{state_names[state_index]}",
            (state_positions_x[state_index], state_positions_y[state_index]),
        )
    else:
        state_guess = StateText()
        state_guess.game_over()
        game_is_on = False


screen.mainloop()
