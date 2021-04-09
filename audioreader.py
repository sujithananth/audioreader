import pyttsx3 #pyttsx3 is a python module used to generate   voices  from text
import PyPDF2  #module used to reads the pdf file

speaker=pyttsx3.init()
    
def read_book(bookname,wh):
    speaker=pyttsx3.init()
    book = open (bookname,'rb') #opening the book in binary to be read  by python pyPDF2
    pdfreader = PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    print("total no of pages :",pages)
    speaker.setProperty('rate', 90)#speed at which the reader speaks
    number=wh-1
    page=pdfreader.getPage(number)  #gets page no from which it has to read
    text=page.extractText() #extracting texts from the pdf
    speaker.say(text)
    speaker.runAndWait()


def write_book(bookname,wh,mpname):
    speaker=pyttsx3.init()
    book = open (bookname,'rb') #opening the book in binary to be read  by python pyPDF2
    pdfreader = PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    print("total no of pages :",pages)
    speaker.setProperty('rate', 90)#speed at which the reader speaks
    number=wh-1
    page=pdfreader.getPage(number)  #gets page no from which it has to read
    text=page.extractText() #extracting texts from the pdf
    speaker.save_to_file(text,mpname+".mp3")
    speaker.runAndWait()

