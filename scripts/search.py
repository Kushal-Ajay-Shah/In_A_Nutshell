from googlesearch import search
from newspaper import Article

def getInfo(URL):
    article = Article(URL, language="en")
    article.download()
    article.parse()
    # print(article.title)
    return article.text, article.top_image, article.publish_date, article.title


def getMeResult(searchQuery):
    info = []
    for url in search(searchQuery, tld="co.in", num=5, stop=5, pause=2):
        text , img, date, title = getInfo(url)
        res = {'url': url, 'text': text, 'image': img, 'date': date, 'title': title}
        info.append(res)    
    return info


