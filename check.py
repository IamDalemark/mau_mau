import PySimpleGUI as sg

# All the stuff inside your window.
sg.popup("MAU MAU")
get_number_str = sg.popup_get_text("How many players: ")
num_of_players = int(get_number_str)

layout = []
player_count = 1
round_count = 1
scores= [0] 
for player in range(0, num_of_players):
    layout.append([sg.Column([[sg.Text(f'Player {player_count} Total Score: {scores[player_count-1]} ', key=f"_SCORE_PLAYER_{player_count-1}"), (sg.Input(default_text='0', key=f'input_{player_count-1}'))]])])
    scores.append(0)
    player_count += 1
button_add = [sg.Button("ADD!")]
layout.append(button_add)
layout.append([sg.Text(f"Round number: {round_count}", key = "_ROUND_NUMBER_")])
# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    if event == 'ADD!':
        round_count += 1
        window["_ROUND_NUMBER_"].update(f"Round number: {round_count}")
        score_count = 0
        for __ in range(0,player_count-1):
            scores[score_count] += int(values[f'input_{score_count}' ])
            window[f"_SCORE_PLAYER_{score_count}"].update(f'Player {score_count+1} Total Score: {scores[score_count]}')
            score_count += 1

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    print(scores[0])
    
window.close()
