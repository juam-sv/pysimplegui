import PySimpleGUI as sg

layout = [
    [sg.Text('Conversion Metrics'), sg.Spin(['item1', 'item2', 'item3'])],
    [sg.Button('Convert')],
    [sg.Input()],
    [sg.Text('Frutas'), sg.Button('Escolher Fruta')],
]

sg.Window('Converter', layout).read()