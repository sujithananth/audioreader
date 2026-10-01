import pyttsx3 #pyttsx3 is a python module used to generate   voices  from text
import pdfext  #module used to reads the pdf file
print("===Audioreader===" )
speaker=pyttsx3.init()
text=pdfext.pdfex()
speaker.setProperty('rate', 90)
z=str(input("'read (R or r)' or 'write to mp3 (W or w)'>>"))
if (z=='r') or (z=='R'):
    #speed at which the reader speaks
    speaker.say(text)
    speaker.runAndWait()
elif (z=='w') or(z=='W'):
    mpname=str(input("enter how to save the mp3 file>>"))
    speaker.save_to_file(text,mpname+".mp3")
    speaker.runAndWait()
else:
    print("oops  error!  try typing correctly ")

