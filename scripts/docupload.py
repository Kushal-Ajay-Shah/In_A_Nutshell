import docx
import io
import PyPDF2

def getDocxText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def getPdfText(file) :
    pdfFileObj = file.read()
    pdfReader = PyPDF2.PdfFileReader(io.BytesIO(pdfFileObj))
    pageObj = pdfReader.getPage(0) 
    print(pageObj.extractText()) 

def getTxtText(file) : 
    contents = file.read()
    print(contents)
    