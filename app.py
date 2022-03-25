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
from scripts.docupload import getText
from scripts.article_similarity import documentSimilarity

app = Flask(__name__)

resl = []
@app.route("/")
def main():
    return render_template('home.html')

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
    similarity_threshold = 0.7
    if request.method == 'POST':
        finalres = []   
        checkedIndices = request.form.getlist('my_checkbox')
        uniqueIndices = []
        global resl
        # print("resl length: ",len(resl))
        for i in range(len(checkedIndices)):
            index_i = int(checkedIndices[i])
            flag = True
            if i==len(checkedIndices)-1:
                uniqueIndices.append(int(checkedIndices[i]))
                break
            for j in range(i+1,len(checkedIndices)):
                index_j = int(checkedIndices[j])
                data_i = resl[index_i]['text']
                data_j = resl[index_j]['text']
                sim_ij = documentSimilarity(data_i, data_j)
                # print("Similarity {} and {}: {}".format(i,j,sim_ij))
                if sim_ij >= similarity_threshold:
                    flag = False
                    break
            if flag:
                uniqueIndices.append(index_i)
        # print("checked: ",checkedIndices)
        # print("unique: ",uniqueIndices)
        for index in uniqueIndices:
            articleNum = index
            print(articleNum)
            resl[articleNum]['summary'] = getSummary(resl[articleNum]['text'])
            finalres.append(resl[articleNum])

        return render_template('summary.html', resl = finalres)

@app.route('/offline',methods = ['POST','GET'])
def offline() :
    if request.method == 'POST' :
        if 'file' not in request.files:
            return 'No file found'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        text = getText(file)
        print(type(text))
        summary = getSummary(text)
        print(summary)
        return render_template('uploadSummary.html',summary = summary)
        # return "success"


    return 'failed'

     
if __name__ == "__main__":
    app.run(debug=True)