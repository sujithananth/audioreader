#webscrap
import PySimpleGUI as sg
import webscrap_backend
sg.theme('darkamber')
layout=[
    [sg.InputText('',size=(70,2),key='url'),sg.Button("get data",font=('courier',20),key='get',bind_return_key=True)],
    [sg.Multiline('',size=(50,15),font=('courier',16),key='out',disabled=True)]
]
def  display_analytics(url):
     html_page=get_html_content(url)
     data=parse_html_page(html_page,'p')
     


if __name__=="__main__":
    Window=sg.Window('webscraper',layout)
    while True:
         event,values =Window.read()
         if event == sg.WINDOW_CLOSED:
            break
         elif event=='get':
             display_analytics(values['url'])
    
    Window.close()