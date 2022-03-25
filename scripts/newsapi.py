# APIKEY=a0c4342d94b44c2fad2461841bcc97ff


# keyword : search string
# searchIn : title,description or content (multiple can also be chosen)
# sources : country (for india : in) check sources index in doc
# fromdate,todate : yyyy-mm-dd
# language : check doc (en for english)
# sortBy : default : publishedAt , options are relevancy(more closely related to q first),popularity(popular sources first),publishedAt(newest first)


import json
from tkinter import NE
import requests    
from bs4 import BeautifulSoup

def clean(list):
    newList=[]
    for dict in list:
        newdict={}
        newdict['url']=dict['url']
        newdict['text']=dict['content']
        newdict['image']=dict['urlToImage']
        newdict['title']=dict['title']
        newdict['date']=dict['publishedAt']
        newList.append(newdict)
    return newList
def NewsApi(keyword='',searchIn='',sources='',fromdate='',todate='',language='',sortBy='relevancy') :
    articlesarr = []
    query_params = {
        'q' : keyword,
        'searchIn' : searchIn,
        'sources' : sources,
        'from' : fromdate,
        'to' : todate,
        'language' : language,
        'sortBy' : sortBy,
        'apiKey' : 'a0c4342d94b44c2fad2461841bcc97ff'
    }
    
    main_url = " https://newsapi.org/v2/everything"
    # fetching data in json format
    res = requests.get(main_url, params=query_params).json()
    # print(res.json())

    
    count = 0
    for article in res['articles'] :
        if count ==5 :
            break
        article.pop('author')
        article.pop('description')

        URL = article['url']
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,'html.parser')
        content = soup.find_all('p')
        str = ''
        counter = 0
        # print(content.text)
        for i in content :
            if len(i.text) > 150 :
                str += i.text
            counter+=1

        article['content'] = str
        
        articlesarr.append(article)

        count+=1
    
    return articlesarr
