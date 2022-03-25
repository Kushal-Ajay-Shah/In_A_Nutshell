from ast import keyword
# from crypt import methods
from distutils.log import debug
from weakref import finalize
from flask import Flask, render_template, redirect, request, url_for
from googlesearch import search
from transformers import RetriBertConfig
from scripts.search import getMeResult 
from scripts.t5_summary import getSummary
from jinja2 import Template
from scripts.newsapi import NewsApi
from scripts.newsapi import clean

app = Flask(__name__)

resl = []
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/ip',methods = ['POST', 'GET'])
def getInfo():
   if request.method == 'POST':
        keyword = request.form['keyword']
        res = getMeResult(keyword)
        newsapires= NewsApi(keyword)
        newsapires = clean(newsapires)
        print(newsapires[0])
        fin=[]
        for i in range(min(5,len(res))):
            fin.append(res[i])
        for i in range(min(5,len(newsapires))):
            fin.append(newsapires[i])
        
        global resl
        resl = fin
        # print(fin)
        return render_template('cards.html', res = resl , reslength = len(resl))

@app.route('/summarize', methods = ['POST', 'GET'])
def summarize():
    if request.method == 'POST':
        finalres = []   
        checkedIndices = request.form.getlist('my_checkbox')
        for index in checkedIndices:
            articleNum = int(index)
            print(articleNum)
            global resl
            resl[articleNum]['summary'] = getSummary(resl[articleNum]['text'])
            finalres.append(resl[articleNum])

        return render_template('summary.html', resl = finalres)

     
if __name__ == "__main__":
    app.run(debug=True, port=8000)