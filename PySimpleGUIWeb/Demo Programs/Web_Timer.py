#!/usr/bin/env python
import PySimpleGUIWeb as sg
import time
import sys

# ----------------  Create Form  ----------------
layout = [
    [sg.Text('', background_color='black')],
    [sg.Text('00:00', size=(30, 1), font=('Helvetica', 30), justification='center', text_color='white', key='text', background_color='black')],
    [sg.Text('', background_color='black')],
    [sg.Button('Pause', key='button', button_color=('white', '#001480')),
     sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
     sg.Exit(button_color=('white', '#8B1A1A'), key='Exit', )],
        ]

window = sg.Window('Running Timer', background_color='black', font='Helvetica 18').Layout(layout)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while (True):
    # --------- Read and update window --------
    if not paused:
        event, values = window.Read(timeout=0)
        current_time = int(round(time.time() * 100)) - start_time
    else:
        event, values = window.Read()
    print(event, values) if event != sg.TIMEOUT_KEY else None
    if event == 'button':
        event = window.FindElement(event).GetText()
    # --------- Do Button Operations --------
    if event is None or event == 'Exit':        # ALWAYS give a way out of program
        break
    if event is 'Reset':
        start_time = int(round(time.time() * 100))
        current_time = 0
        paused_time = start_time
    elif event == 'Pause':
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window.FindElement('button')
        element.Update(text='Run')
    elif event == 'Run':
        paused = False
        start_time = start_time + int(round(time.time() * 100)) - paused_time
        element = window.FindElement('button')
        element.Update(text='Pause')

    # --------- Display timer in window --------
    window.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))
# --------- After loop --------
window.Close()
print('after loop')
sys.exit()