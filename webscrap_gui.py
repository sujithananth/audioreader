#webscrap
import PySimpleGUI as sg
sg.theme('darkamber')
layout=[
    [sg.InputText('',size=(30,10),font=('courier',16),key='book name'),sg.Button("enter book name")],
    [sg.InputText('',size=(70,2),key='url'),sg.Button("get data",font=('courier',20),key='get',bind_return_key=True)],
    
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