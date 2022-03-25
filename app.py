from ast import keyword
# from crypt import methods
from distutils.log import debug
from nntplib import ArticleInfo
from flask import Flask, render_template, redirect, request, url_for
from googlesearch import search
from scripts.search import getMeResult 
from scripts.t5_summary import getSummary
from jinja2 import Template

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
        checkedIndices = request.form.getlist('my_checkbox')
        articleNum = int(checkedIndices[0])
        global resl
        summary = getSummary(resl[articleNum]['text'])
        return summary
     
if __name__ == "__main__":
    app.run(debug=True, port=8000)