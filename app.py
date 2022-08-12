# from crypt import methods
# from distutils.log import debug
# from googlesearch import search
# from transformers import RetriBertConfig
# from jinja2 import Template

from weakref import finalize
from flask import Flask, render_template, redirect, request, url_for

from scripts.info import getSearchResult
from scripts.summary import getSummaryResult
from scripts.docupload import getText
from scripts.utils.summary.t5_summary import getSummary

app = Flask(__name__)

resl = []
@app.route("/")
def main():
    return render_template('home.html')

@app.route('/showArticles',methods = ['POST', 'GET'])
def getInfo():
   if request.method == 'POST':
        global resl

        keyword = request.form['keyword']
        resl = getSearchResult(keyword)

        return render_template('cards.html', res = resl , reslength = len(resl))

@app.route('/summarize', methods = ['POST', 'GET'])
def summarize():

    if request.method == 'POST':
        global resl
        
        checkedIndices = request.form.getlist('my_checkbox')
        finalres = getSummaryResult(checkedIndices, resl)

        return render_template('summary.html', resl = finalres , reslength = len(finalres))

@app.route('/offline',methods = ['POST','GET'])
def offline() :
    if request.method == 'POST' :
        if 'file' not in request.files:
            return 'No file found'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        text = getText(file)
        summary = getSummary(text)
        return render_template('uploadSummary.html',summary = summary)

    return 'failed'

     
if __name__ == "__main__":
    app.run()
    # app.run(debug=True)


## Tasks ToDo:
# - UI:
    # [] Incase no info found? Not found page
    # [] Mobile Responsive UI
    # [] Cards Image size fixture
    # [] Cards Checkbox fix
# - Please reduce search time. Its slower than any search engine : Embedd a search engine page?