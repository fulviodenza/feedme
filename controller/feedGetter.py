import sys
sys.path.append('..')
import twitterGetter
import googleNewsGetter
import time
from datetime import datetime as dt

#function to get news from tweets
def twitter_res(listTweets):
    tweetList, secondListT = zip(*listTweets)
    dt_listT = []
    
    for i in range(10):
        dt_listT.append(dt.strptime(secondListT[i],'%a %b %d %H:%M:%S +0000 %Y'))

    listTweets = list(zip(tweetList, dt_listT))

    #for j in range(10):
    #    print(listTweets[j][0])
    return listTweets

#function to get news from google
def google_res(listNews):
    newsList, secondListG = zip(*listNews)
    dt_listG = []

    #Conversion of datetime
    for i in range(10):
        dt_listG.append(dt.strptime(secondListG[i],'%Y-%m-%dT%H:%M:%SZ'))

    listNews = list(zip(newsList, dt_listG))
    #for k in range(10):
    #    print(listNews[k][0])
    return listNews