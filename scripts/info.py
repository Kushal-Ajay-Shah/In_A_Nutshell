from .utils.search.search import getMeGoogleResult
from .utils.search.newsapi import NewsApi,clean


def getSearchResult(keyword):
    res = []
    newsapires = []
    res = getMeGoogleResult(keyword)
    newsapires= NewsApi(keyword)
    newsapires = clean(newsapires)
    fin=[]
    for i in range(min(5,len(res))):
        fin.append(res[i])
    for i in range(min(5,len(newsapires))):
        fin.append(newsapires[i])

    return fin