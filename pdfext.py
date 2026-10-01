import PyPDF2
def pdfex():
    Pdfname=str(input("book name:",)+".pdf")
    pdf1 = open (Pdfname,'rb') #opening the book in binary to be read  by python pyPDF2
    pdfreader = PyPDF2.PdfReader(pdf1)
    pages=len(pdfreader.pages)
    print("total no of pages :",pages)
    page=pdfreader.pages[int(input("enter which page u want:"))]
    text=page.extract_text()
    print(text)
    return text
