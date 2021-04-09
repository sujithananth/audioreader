
import PySimpleGUI as sg
import audioreader
sg.theme('dark black')
layout=[
     [sg.Text('Filename',font=('courier',16))], [sg.Input('',size=(50,3),key='book'), sg.FileBrowse()],
     [sg.Text('enter page number to be read'),sg.InputText('',key=('page no'))],
     [sg.Button("read",key=('read')),sg.Button("write",key=('write')), sg.Button("clear",key=('clear'))]
    
]


Window=sg.Window('webscraper',layout)
while True:
    event,values =Window.read()
    if event == sg.WINDOW_CLOSED:
            break
    elif event == 'read':
          audioreader.read_book(values['book'],int(values['page no']))
    elif event == 'write':
          sg.Window("enter the mp3 name of file you want to save",[sg.InputText('',key=('mp3 name')),sg.Button("ok")])
          eve,val=Window.read()
          audioreader.write_book(values['book'],int(values['page no']),str(val['mp3 name']))

Window.close()