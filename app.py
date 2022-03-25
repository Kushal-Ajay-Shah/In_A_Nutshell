from ast import keyword
# from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, redirect, request, session, url_for
from googlesearch import search
from scripts.search import getMeResult 
from scripts.newsapi import NewsApi
from scripts.newsapi import clean
#from scripts.t5_summary import getSummary
from jinja2 import Template

app = Flask(__name__)

resL = []
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/ip',methods = ['POST', 'GET'])
def getInfo():
    if request.method == 'POST':
        keyword = request.form['keyword']
        res = getMeResult(keyword)
        print(res[0])
        newsapires= NewsApi(keyword)
        newsapires = clean(newsapires)
        print(newsapires[0])
        fin=[]
        for i in range(5):
            fin.append(res[i])
            fin.append(newsapires[i])
        
        global resL
        resL = fin
        #print(res[0].keys())
        # s = getSummary(res[2]['text'])
        # print("text: ",res[2]['text'])
        # print("summary:",s)
        # titles = [r['title'] for r in res]
        # print("\n".join(titles))
        return render_template('cards.html', res = fin)
    return 0

@app.route('/summarize', methods = ['POST', 'GET'])
def summarize():
    if request.method == 'POST':
        checkedIndices = request.form.getlist('my_checkbox')
        print(checkedIndices)
        global resL
        print(resL)
        return "\n".join(checkedIndices)
     
if __name__ == "__main__":
    app.run(debug=True, port=8000)