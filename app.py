from ast import keyword
# from crypt import methods
from distutils.log import debug
from nntplib import ArticleInfo
from flask import Flask, render_template, redirect, request, url_for
from googlesearch import search
from scripts.docUpload import getText
from scripts.search import getMeResult 
from scripts.t5_summary import getSummary
from jinja2 import Template

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


resl = []

@app.route("/")
def main():
    return render_template('index2.html')

@app.route('/ip',methods = ['POST', 'GET'])
def getInfo():
   if request.method == 'POST':
        keyword = request.form['keyword']
        res = getMeResult(keyword)
        global resl
        resl = res
        # print(res)
        # s = getSummary(res[2]['text'])
        # print("text: ",res[2]['text'])
        # print("summary:",s)
        # titles = [r['title'] for r in res]
        # print("\n".join(titles))
        return render_template('cards.html', res = res)

@app.route('/summarize', methods = ['POST', 'GET'])
def summarize():
    if request.method == 'POST':
        finalres = []   
        checkedIndices = request.form.getlist('my_checkbox')
        for index in checkedIndices:
            articleNum = int(index)
            print(articleNum)
            global resl
            print(resl)
            resl[articleNum]['summary'] = getSummary(resl[articleNum]['text'])
            finalres.append(resl[articleNum])
        return render_template('summary.html', resl = finalres)

@app.route('/upload')
def upload():
    return render_template('uploadPdf.html')

@app.route('/offline',methods = ['POST','GET'])
def offline() :
    if request.method == 'POST' :
        if 'file' not in request.files:
            return 'No file found'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        return getText(file)
        # return "success"


    return 'failed'
     
if __name__ == "__main__":
    app.run(debug=True, port=8000)