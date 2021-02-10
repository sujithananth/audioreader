# audioreader
audioreader =reads pdf books files for me 
there is a file named pyt.pdf in the book shelf

lets  get started:
 1.first install the modeules we need 
   
   pip install pyttsx3

   pip install pyPDF2

2.import them to the code,write the code in the python file
   
   import pyttsx3
   imort pyPDF2

3.first check whether our pyttsx3 is working by typing the following code and run it.
   
   speaker=pyttsx3.init()
   speaker.setProperty('rate', 90)
   speaker.say("hi")
   speaker.runAndWait()
if it worked  and  u can hear the voice  the move on to the next step

4.write code for pyPDF2 to make python open and read  pdf files,
   
   bookname=input("enter the book name :",)
   book = open (bookname,'rb')
   pdfreader = PyPDF2.PdfFileReader(book)
   pages=pdfreader.numPages
   print("total no of pages :",pages)
if the above code works then u ll get the no of pages hence pyPDF2 is working and it opens  and reads the pdf

5.then write these two lines  and change  the speaker.say()  
   page=pdfreader.getPage(22)
   text=page.extractText()
   speaker.say(text)
if the above works then ur code will read ur book and u can hear the voice

  
to know the details of the code look into code comments on python file...
u can read  any pdf file but it should be in the current location of this folder  ...
