import numpy as np
import pandas as pd
import PyPDF2

# creating a pdf file object
pdfFileObj = open('assets/CS.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
  
# creating a page object
pageObj = pdfReader.getPage(0)
  
# # extracting text from page
print(pageObj.extractText())
  
# closing the pdf file object
pdfFileObj.close()