import PySimpleGUI as sg
import pyttsx3
engine = pyttsx3.init()
# All the stuff inside your window.
sg.popup("MAU MAU!")
def run():
    try:
      get_number_str = sg.popup_get_text("Number of players: ")
      num_of_players = int(get_number_str)
      return num_of_players
    except ValueError:
        sg.popup("please enter a valid number!")
        return run()
num_of_players = run()

layout = []
player_count = 1
round_count = 1

#where the scores are caculated
scores= [0] 
names = []

#no. of columns to be made
for player in range(0, num_of_players):
    #where the name gets entered  to the list
    name = sg.popup_get_text(f"Enter player {player_count} name: ")
    names.append((str(name).capitalize()).strip())
    #displays!
    layout.append([sg.Column([[sg.Text(f'{names[player_count-1]} total Score: {scores[player_count-1]} ', key=f"_SCORE_PLAYER_{player_count-1}"), (sg.Input(default_text='0', key=f'input_{player_count-1}'))]])])
    scores.append(0)
    player_count += 1

layout.append([sg.Text(f"Current round: {round_count}", key = "_ROUND_NUMBER_")])
layout.append([sg.Column([[sg.Button("END CURRENT ROUND!")]])])
scores.remove(scores[-1])
# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process     "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    if event == 'END CURRENT ROUND!':
        engine.say(f"Round number {round_count}")
        round_count += 1
        score_count = 0


        for __ in range(0,player_count-1):
            try:
                input_score = int(values[f'input_{score_count}'])
                scores[score_count] += input_score
                window[f'input_{score_count}'].update('0')
                window[f"_SCORE_PLAYER_{score_count}"].update(f'{names[score_count]} total Score: {scores[score_count]} ')
                engine.say(f'{names[score_count]} total Score: {scores[score_count]} ')
                score_count += 1
# error input handling
            except ValueError:
                sg.popup("please enter a valid number!")
                round_count -= 1
                break
        lead_score = min(scores)
        lead_score_index  = scores.index(lead_score)
        engine.say(f"{names[lead_score_index]} is in the first place with the score of {lead_score}")
        engine.runAndWait()
        window["_ROUND_NUMBER_"].update(f"Current round: {round_count}")
        

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

window.close()
