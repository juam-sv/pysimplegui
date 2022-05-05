import PySimpleGUI as sg
from pathlib import Path

emotions=[
    'happy', [':-)',':D','<3', '*-*'],
    'sad',[':(','T_T', ':('],
    'other',[':3', ':V', ':/']
]

emotions_events = emotions[1] + emotions[3] + emotions[5]

menu_layout = [
    ['File', ['Open', 'Save', '----', 'Exit']],
    ['Tools', ['Word Count', 'Help']],
    ['Add', emotions]
]

sg.theme('DarkPurple4')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Not Save', key='-DOC_NAME-')],
    [sg.Multiline(no_scrollbar=True, size = (40,20), key='-TEXTBOOK-')],
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'Word Count':
        sg.popup('Word Count:', len(values['-TEXTBOOK-'].split()))

    if event in emotions_events:
        all_text = values['-TEXTBOOK-'] + ' ' + event
        window['-TEXTBOOK-'].update(all_text)


    if event == 'Open':
        file_path = sg.popup_get_file('Open File', no_window=True)
        if file_path is not None:
            file = Path(file_path)
            window['-TEXTBOOK-'].update(file.read_text())
            window['-DOC_NAME-'].update(file.name)

    #save and open events
    if event == 'Save':
        file_path = sg.popup_get_file('Save File', no_window= True, save_as=True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOOK-'])
        window['-DOC_NAME-'].update(file.name)

window.close()
