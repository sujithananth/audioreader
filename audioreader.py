import pyttsx3 #pyttsx3 is a python module used to generate   voices  from text
import PyPDF2  #module used to reads the pdf files
bookshelf=['pyt.pdf']
print("the books in bookshelf is :",bookshelf)
ad=input("do u want to add book to the shelf?  type yes or no :",)
if (ad=="yes" )or (ad=="YES"):
    bn=input("enter the name with .pdf :",)
    bookshelf.append(bn)
else:
    print("~~~~~~~~~~~~~~~~~~") 
bookname=str(input("enter the book name with .pdf:",))
speaker=pyttsx3.init()
    
z=str(input("what u want to do  'read' or 'write to mp3'>>"))
if (z=='read') or (z=='READ'):
    book = open (bookname,'rb') #opening the book in binary to be read  by python pyPDF2
    pdfreader = PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    print("total no of pages :",pages)
    speaker.setProperty('rate', 90)#speed at which the reader speaks
    wh=int(input("enter which page u want:"))
    number=wh-1
    page=pdfreader.getPage(number)  #gets page no from which it has to read
    text=page.extractText() #extracting texts from the pdf
    speaker.say(text)
    speaker.runAndWait()
elif (z=='write to mp3') or(z=='write'):
    book = open (bookname,'rb') #opening the book in binary to be read  by python pyPDF2
    pdfreader = PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    print("total no of pages :",pages)
    speaker.setProperty('rate', 90)#speed at which the reader speaks
    wh=int(input("enter which page u want:"))
    number=wh-1
    page=pdfreader.getPage(number)  #gets page no from which it has to read
    text=page.extractText() #extracting texts from the pdf
    mpname=str(input("enter how to save the mp3 file>>"))
    speaker.save_to_file(text,mpname+".mp3")
    speaker.runAndWait()
else:
    print("oops  error!  try typing correctly ")

