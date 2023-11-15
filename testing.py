import PySimpleGUI as sg

sg.theme('DarkAmber') 

layout = [  [sg.Text('Some text on Row 1', key='text')],
            [sg.Button('Next'), sg.Button('exit')] ]


window = sg.Window('Window Title', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'exit':
        break
    else: 
        window['text'].update("Some different text")

window.close()