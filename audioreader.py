import pyttsx3 #pyttsx3 is a python module used to generate   voices  from text
import PyPDF2  #module used to reads the pdf files
bookshelf=['pyt.pdf']
print("the books in bookshelf is :",bookshelf)
ad=input("do u want to add book to the shelf?  type yes or no :",)
if ad==("yes" or "YES"):
    bn=input("enter the name with .pdf :",)
    bookshelf.append(bn)
else:
    print("okay you can proceed:")
    
bookname=input("enter the book name :",)
book = open (bookname,'rb') #opening the book in binary to be read  by python pyPDF2
pdfreader = PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print("total no of pages :",pages)
print("the ebook reading now is :",bookname)
speaker=pyttsx3.init() #initialise the speaker engine 
speaker.setProperty('rate', 90)#speed at which the reader speaks
page=pdfreader.getPage(22)  #gets page no from which it has to read
text=page.extractText() #extracting texts from the pdf
speaker.say(text)
speaker.runAndWait()


