import re
import docx
import io
import PyPDF2
ALLOWED_EXTENSIONS = {'txt', 'pdf','docx'}



#**********************
def get_ascii(text) :
    return  ''.join([i if ord(i) < 128 else '' for i in text])
    #  return unidecode(unicode(text, encoding = "utf-8"))


def check_ascii(text) :
    return text.isascii()


def remove_chars(text) :
    newlabel = re.sub('[^A-Za-z0-9\.\!\?\"\,\'\:\;\-\&]+', ' ', text)
    print(newlabel)
    return newlabel
#*********************




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    return pageObj.extractText()


def getTxtText(file) : 
    contents = file.read()
    print(contents)
    text = get_ascii(contents.decode("utf-8"))
    newtext = remove_chars(text)
    print(newtext)
    return newtext 
    

def getText(file):
    if file and allowed_file(file.filename):
        filetype = file.filename.rsplit('.',1)[1].lower()
        if filetype == 'docx' :
            return getDocxText(file)
        elif filetype == 'pdf' :
            return getPdfText(file)
        elif filetype == 'txt' :
            return getTxtText(file)
    return 'error'