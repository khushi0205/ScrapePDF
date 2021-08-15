# program to extract data from a PDF file

from PyPDF2 import PdfFileReader
pdfFileObj = PdfFileReader('PBL_ASKFH53,FH37,FH42.pdf')

for page_num in range(pdfFileObj.numPages):
    print('Page: {0}'.format(page_num))
    pobj = pdfFileObj.getPage((page_num))

    try:
         txt  = pobj.extractText()
         print(txt)
    except:
         pass