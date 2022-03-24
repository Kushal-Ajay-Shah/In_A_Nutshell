from ast import keyword
from distutils.log import debug
from flask import Flask, render_template, redirect, request, url_for
from googlesearch import search
from scripts.search import getMeResult 
from jinja2 import Template


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/ip',methods = ['POST', 'GET'])
def getInfo():
   if request.method == 'POST':
        keyword = request.form['keyword']
        res = getMeResult(keyword)
        # print(res)
        titles = [r['title'] for r in res]
        print("\n".join(titles))
        return render_template('cards.html', result =  res)

if __name__ == "__main__":
    app.run(debug=True, port=8000)