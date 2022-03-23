from ast import keyword
from distutils.log import debug
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/ip',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
        keyword = request.form['keyword']
        print(keyword)
        return "<p>Hello</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)