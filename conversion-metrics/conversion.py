import PySimpleGUI as sg

layout = [
    [sg.Text('Conversion Metrics', \
    enable_events = True, \
    key = '-TEXT-'), \
    sg.Spin(['item1', 'item2', 'item3'])],
    [sg.Button('Convert', key='-BUTTON1-')],
    [sg.Input()],
    [sg.Text('Frutas'), sg.Button('Escolher Fruta', key='-BUTTON2-')],
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        print('Convertendo...')
    
    if event == '-BUTTON2-':
        print('Revertando...')

    if event == '-TEXT-':
        print('TEXTO...')

window.close()
