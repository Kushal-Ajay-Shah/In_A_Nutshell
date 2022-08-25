# import the module
import tweepy
from .utils.tokens import *
# def getTop
def get50Trends(woeid = 23424848):
    # Default 23424848 -> woeid of India
# authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # set access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

    # calling the api
    api = tweepy.API(auth)

    # WOEID of London
    # woeid = 44418
    # woeid = 2295411 #Mumbai
    # woeid = 2295424 #Chennai
    # woeid = 23424848
    # fetching the trends
    trends = api.get_place_trends(id = woeid)

    # printing the information
    # print("The top trends for the location are :")
    returnList = []
    for value in trends:
        for trend in value['trends']:
            # print(trend['name'])

            returnList.append(trend['name'])
    return returnList
    # print(returnList)

print(get50Trends())