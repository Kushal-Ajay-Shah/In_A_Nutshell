from logging import exception
from googlesearch import search
from newspaper import Article
from bs4 import BeautifulSoup
import requests


def getInfo(URL):
    # response = requests.get(URL)
    # soup = BeautifulSoup(response.content, "html.parser" )
    # return(soup.find('title').string)
    article = Article(URL, language="en")
    try: 
        article.download()
        article.parse()
        return article.text, article.top_image, article.publish_date, article.title
    except:
        print("error")
        return 'a','a','a','a'


    # print(article.title)


# def getMeResult(searchQuery):
#     info = []
#     for url in search(searchQuery, tld="co.in", num=5, stop=5, pause=2):
#         text , img, date, title = getInfo(url)
#         res = {'url': url, 'text': text, 'image': img, 'date': date, 'title': title}
#         info.append(res)    
#     return info


def getMeResult(query):
    URL = "https://www.google.com/search?q="
    # print(URL+query.replace(' ','+'))
    response = requests.get(URL+query.replace(' ','+'))
    soup = BeautifulSoup(response.content, "html.parser" )
    # print(soup.prettify())
    links = []
    for link in soup.body.find_all('a',href=True):
        if link.has_attr('href') and link['href'][:4] == '/url' :
            i = link['href'][7:].find("&sa")
            links.append(link['href'][7:][:i])
    links = filter(lambda x: 'twitter' not in x,links)
    links = filter(lambda x: 'youtube' not in x,links)
    links = list(filter(lambda x: 'linkedin' not in x,links))
    # for l in links: 
    #     print(l)
    info = []
    # print(links)
    for url in links[:5]:
        # print(getInfo(url))
        text, img, date, title = getInfo(url)
        res = {'url': url,'text': text, 'image':img, 'date':date, 'title': title}
        info.append(res)    
    return info

# getMeResult(input("input: "))
