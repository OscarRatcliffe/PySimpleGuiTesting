import PySimpleGUI as sg
import datetime

sg.theme('Dark Amber')  # Let's set our own color theme

#Sets a start time
def getstart():
    start = datetime.datetime.now()
    start = start.timestamp()
    return start

#Updates age using start time
def update(start):
    age = datetime.datetime.now()
    age = age.timestamp()
    age = age-start
    return int(age)

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
#Notice the window element is in the main code and therefore has global scope
#Because it is a list (mutable) it can be updated from within the function.
#Of course you need to call the function after defining the window.
        
health = 0
start = getstart()
age = 0
R="red"
B="blue"
b = "black"

ill = [
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,B,B,R,R,R],
        [R,R,R,B,B,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R]
        ]
dead = [
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,b,b,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R]
        ]
well = [
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,B,R,R,B,R,R],
        [R,R,R,B,B,R,R,R],
        [R,R,R,B,B,R,R,R],
        [R,R,B,R,R,B,R,R],
        [R,R,R,R,R,R,R,R],
        [R,R,R,R,R,R,R,R]
        ]

        
ill = led_gen(ill)
well = led_gen(well)
dead = led_gen(dead)

win_ill = sg.Column(ill, visible = False,  key = 'ILL')
win_well = sg.Column(well, visible = False,  key = 'WELL')
win_dead = sg.Column(dead, visible = True,  key = 'DEAD' )

#These are the keys of each column
possible_wins = ['ILL', 'WELL', 'DEAD'] 
layout = [[sg.Text("Health: " +str(health),size=(10,1), key = 'HLT'), sg.Text("Age: "+str(age),size = (10,1), key = 'AGE')],
          [win_ill,win_well,win_dead],
          [sg.Button("Well", size = (4,1)),sg.Button("Ill", size =(4,1)),sg.Button("Dead", size =(4,1))]]

#STEP 2 - create the window
window = sg.Window("Ressy Bug", layout , element_justification = 'center' )

# STEP3 - the event loop
while True:
    event, values = window.read(timeout = 10)
    print(event, values) 
    if event == sg.WIN_CLOSED:     
      break
    elif event == "Well":
        switch('WELL')
        health = 90
    elif event == "Ill":
        switch('ILL')
        health = 20
    elif event == "Dead":
        switch('DEAD')
        health = 0
        
    age = update(start)
    window['AGE'].update("Age: " +str(age))
    window['HLT'].update("Health: " +str(health))
       
    
window.close()