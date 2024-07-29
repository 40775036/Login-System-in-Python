import PySimpleGUI as sg
import Login_main

# All the stuff inside your window.
layout = [  [sg.Button('register')] ,
            [ sg.Button('login')],
            [ sg.Button('Cancel')]
              ]

# Create the Window
window = sg.Window('Login System', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'register':
        Login_main.register()
        


    if event=='login':
        Login_main.login()

    print('Hello', values[0], '!')

window.close()