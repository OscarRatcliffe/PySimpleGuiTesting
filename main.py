import PySimpleGUI as sg
import datetime

sg.theme('Dark Amber')  # Let's set our own color theme

#Generates a tiled image from the textual list
def led_gen(image):
    layout = []
    for column in range(8):
        section =[]
        for row in range(8):
            led = sg.Text(' ', background_color = (image[column][row]), size = (2,1), font = "Courier", pad =(1,1))
            section.append(led)
        layout.append(section)
    return layout

#Switches the required column on and all others off
def switch(activate):
    for key in possible_wins:
        if key == activate:
            window[key].update(visible = True)
        else:
            window[key].update(visible = False)

R="red"
B="blue"
b = "black"

zeroth = [
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]
]

first = [
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,R,R,b,b,b],
        [b,b,b,R,R,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]
        ]
second = [
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,R,R,R,R,b,b],
        [b,b,R,R,R,R,b,b],
        [b,b,R,R,R,R,b,b],
        [b,b,R,R,R,R,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]
        ]
third = [
        [b,b,b,b,b,b,b,b],
        [b,R,R,R,R,R,R,b],
        [b,R,R,R,R,R,R,b],
        [b,R,R,R,R,R,R,b],
        [b,R,R,R,R,R,R,b],
        [b,R,R,R,R,R,R,b],
        [b,R,R,R,R,R,R,b],
        [b,b,b,b,b,b,b,b]
        ]


zeroth_gen = led_gen(zeroth)     
first_gen = led_gen(first)
second_gen = led_gen(second)
third_gen = led_gen(third)

win_zeroth = sg.Column(zeroth_gen, visible = True,  key = 'Zeroth')
win_first = sg.Column(first_gen, visible = True,  key = 'First')
win_second = sg.Column(second_gen, visible = False,  key = 'Second')
win_third = sg.Column(third_gen, visible = False,  key = 'Third' )

#These are the keys of each column
possible_wins = ['Zeroth', 'First', 'Second', 'Third'] 
layout = [
          [win_zeroth, win_first,win_second,win_third],
          [sg.Button("0th", size = (5,1)),sg.Button("1st", size = (5,1)),sg.Button("2nd", size =(5,1)),sg.Button("3rd", size =(5,1))]]

#STEP 2 - create the window
window = sg.Window("Ressy Bug", layout , element_justification = 'center' )

# STEP3 - the event loop
while True:
    event, values = window.read(timeout = 10)
    print(event, values) 
    if event == sg.WIN_CLOSED:     
      break
    elif event == "0th":
        switch('Zeroth')
    elif event == "1st":
        switch('First')
    elif event == "2nd":
        switch('Second')
    elif event == "3rd":
        switch('Third')

           
    
window.close()