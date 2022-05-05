import PySimpleGUI as sg

layout = [
    [sg.Text('Conversion Metrics')],
    [
        sg.Input(key='-INPUT-'), 
        sg.Spin(['KM/Miles', 'Hours/Minutes', 'Celsius/fahrenheit'], key='-UNITS-')
    ],
    [
        sg.Text('Result: '), 
        sg.Text('', key='-RESULT-'),
        sg.Button('Convert', key='-B_CONVERT-')
    ]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-B_CONVERT-':
        input_values = values['-INPUT-']
        if input_values.isnumeric():
            match values['-UNITS-']:
                case 'KM/Miles':
                    result = round(float(input_values) * 0.621371, 2)
                    result_string = f'{input_values} KM = {result} Miles'
                case 'Hours/Minutes':
                    result = round(float(input_values) * 60, 2)
                    result_string = f'{input_values} Hours = {result} Minutes'
                case 'Celsius/fahrenheit':
                    result = round(float(input_values) * 1.8 + 32, 2)
                    result_string = f'{input_values} Graus Celsius= {result} Fahrenheit'
            window['-RESULT-'].update(result_string)
        else:
            result_string = 'Please enter a number'
            window['-RESULT-'].update(result_string)

window.close()
