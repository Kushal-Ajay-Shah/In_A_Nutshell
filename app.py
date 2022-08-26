# from crypt import methods
# from distutils.log import debug
# from googlesearch import search
# from transformers import RetriBertConfig
# from jinja2 import Template

from ast import keyword
from weakref import finalize
from flask import Flask, render_template, redirect, request, url_for
from scripts.get50TrendsDeploy import get50Trends

from scripts.info import getSearchResult
from scripts.summary import getSummaryResult
from scripts.docupload import getText
from scripts.tweepyDeploy import getTweetsText
from scripts.utils.summary.pegasus_summary import getSummary

app = Flask(__name__)

resl = []
keyword = ""
@app.route("/")
def main():
    # trends = get50Trends()[:10]
    base = "/getTweetSummary/"
    trends = [{'url': base + 'politics' , 'text': "Politics"},{'url': base + "tech", 'text': "Tech"},{'url': base + "sports", 'text': "Sports"}, {'url': base + 'finance', 'text': 'Finance'}]
    return render_template('index.html',trends = trends)

@app.route('/showArticles',methods = ['POST', 'GET'])
def getInfo():
   if request.method == 'POST':
        global resl

        global keyword
        keyword = request.form['keyword']
        resl = getSearchResult(keyword)


        return render_template('cards.html', res = resl , reslength = len(resl))

@app.route('/summarize', methods = ['POST', 'GET'])
def summarize():

    if request.method == 'POST':
        global resl,keyword
        
        finalres = []
        checkedIndices = request.form.getlist('my_checkbox')
        # finalres = getSummaryResult(checkedIndices, resl)
        print(keyword)
        tweetText,isVerified = getTweetsText(keyword)
        print(isVerified)
        if tweetText: 
            tweetSummary = getSummary(tweetText).capitalize()
            finalres.append({'url':"https://twitter.com/",'image': "data:image/png;base64,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",'title': 'What Twitter says about '+ keyword,'summary': tweetSummary})

        return render_template('summary.html', resl = finalres , reslength = len(finalres),notVerified = not isVerified)


@app.route('/offline',methods = ['POST','GET'])
def offline() :
    if request.method == 'POST' :
        if 'file[]' not in request.files:
            return 'No file found'
        uploaded_files = request.files.getlist("file[]")
        print(uploaded_files)
        summaries = []
        for file in uploaded_files :
            if file.filename == '':
                return 'No selected file'
            text = getText(file)
            summary = getSummary(text)
            summaries.append({'summary':summary,'title':file.filename})

        print(summaries)
        return render_template('uploadSummary.html',titel = "Your summary is here",summaries = summaries)

    return 'failed'

@app.route('/getTweetSummary/<string:trend>')
def tweetSum(trend):
    trend = trend.replace("%20"," ")
    print(trend)
    tweetText,isVerified = getTweetsText(trend,25)
    if tweetText: 
        summary = getSummary(tweetText).upper()
        return render_template('uploadSummary.html', title="What Twitter says about "+trend,summary = summary, notVerified = not isVerified )
    else:
        return "No Tweets :("



     
if __name__ == "__main__":
    # app.run()
    app.run(debug=True)


## Tasks ToDo:
# - UI:
    # [] Incase no info found? Not found page
    # [] Mobile Responsive UI
    # [] Cards Image size fixture
    # [] Cards Checkbox fix
# - Please reduce search time. Its slower than any search engine : Embedd a search engine page?