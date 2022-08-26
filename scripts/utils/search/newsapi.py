# APIKEY=a0c4342d94b44c2fad2461841bcc97ff
#APIKEY2=42df420094f148aea3f3b301761da31b


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
        'apiKey' : '181835a29ee74ec492a770c2aa0442a7'
    }
    
    main_url = " https://newsapi.org/v2/everything"
    # fetching data in json format
    res = requests.get(main_url, params=query_params).json()

    count = 0
    for article in res['articles'] :
        if count == 2 :
            break
        article.pop('author')
        article.pop('description')

        URL = article['url']
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,'html.parser')
        content = soup.find_all('p')
        str = ''
        counter = 0
        for i in content :
            if len(i.text) > 150 :
                str += i.text
            counter+=1

        article['content'] = str
        
        articlesarr.append(article)

        count+=1
    
    return articlesarr