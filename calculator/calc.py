from tkinter import font
import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Calibre 16', button_element_size= (3, 1), margins=(0, 0), border_width=0)
    button_size = (3, 1)
    layout = [
        [
            sg.Text(
                'Result: ', 
                font = 'Calibre 16', 
                justification='right', 
                expand_x = True, 
                pad = (5, 12),
                right_click_menu = menu_theme,
                key = '-DISPLAY-')

        ],
        [sg.Button('Clear', expand_x= True), sg.Button('Calc', expand_x= True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('/', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('*', size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x= True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)]
    ]  
    return  sg.Window('CALCULATOR', layout)


menu_theme = ['menu',['DarkPurple1', 'BluePurple', 'DarkBlue7', 'random']]
window = create_window('dark')

# lists for the numbers and operators
display_numbers = []

while True:
    event, values = window.read()\

    if event == sg.WIN_CLOSED:
        break
    
    if event in menu_theme[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        display_numbers.append(event)
        str_display_numbers = ''.join(display_numbers)
        window['-DISPLAY-'].update(str_display_numbers)
        

    if event in ['+', '-', '*', '/']:
        print(event)

    if event == 'Calc':
        print(event)

    if event == 'Clear':
        print(event)
        
window.close()
