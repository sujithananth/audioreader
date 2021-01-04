import pyttsx3
import PyPDF2
bookshelf=['pyt.pdf',]
print("the books in bookshelf is :",bookshelf)
ad=input("do u want to add book to the shelf?  type yes or no :",)
if ad==("yes" or "YES"):
    bn=input("enter the name with .pdf :",)
    bookshelf.append(bn)
else:
    print("okay you can proceed:")
    
bookname=input("enter the book name :",)
book = open (bookname,'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print("total no of pages :",pages)
print("the ebook reading now is :",bookname)
speaker=pyttsx3.init()
speaker.setProperty('rate', 90)
page=pdfreader.getPage(22)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()


