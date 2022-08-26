# import the module
import tweepy
from .utils.tokens import *

# fetching the trends
def getTweetsText(seedWord,maxTweets = 100):
    #AUTH PART===========================================
    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # set access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

    # calling the api
    api = tweepy.API(auth)

    client = tweepy.Client(bearer_token)
    #AUTH ENDS=================================

    filters = " lang:en is:verified -is:retweet"
    DefaultQuery ="NDTV adani"+filters
    query= seedWord + filters
    response = client.search_recent_tweets(query,max_results=maxTweets)
    returnText = ""
    isVerified = True

    if not response.data:
        response = client.search_recent_tweets(seedWord,max_results=maxTweets)
        isVerified = False


    for value in response.data:
        
        line=value.text
        # line="The Daily Rip India is back! Here's a &amp quick roundup of today's top stories: Markets collapse in final hour to end near day’s low A break down of Adani's hostile takeover of NDTV Dreamfolks Services IPO open for subscription Read this and more here: https://t.co/H8AvR3o4Fs"
        text_encode = line.encode(encoding="ascii", errors="ignore")
        # decoding the text
        text_decode = text_encode.decode()
        # cleaning the text to remove extra whitespace 
        line = " ".join([word for word in text_decode.split()])
        # print(clean_text)

        line = line.replace("#"," ")
        line = line.replace("@","")
        line = line.replace('|',"")
        line = line.replace('&amp',"")
        line = line.replace('&gt',"")
        # print(line)
        
        arrOfWords = line.split()
        arrOfWords2 = arrOfWords.copy()
        for i,word in enumerate(arrOfWords):
            if(word.find("https")!=-1):
                arrOfWords2.remove(word)
        line = " ".join(arrOfWords2) + " "
        # print(line)
        # print(arrOfWords2)
        # print('='*50)
        returnText = returnText + line
    return returnText, isVerified