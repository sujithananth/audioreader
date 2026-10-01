import pdfext
extracted_text=pdfext.pdfex()
with open(str(input("output name",)+".txt"), 'w', encoding='utf-8') as file:
    file.write(extracted_text)