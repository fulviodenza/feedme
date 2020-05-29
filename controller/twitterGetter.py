import requests
from decouple import config
from requests_oauthlib import OAuth1

auth = OAuth1(
    config('CONSUMER_KEY'), 
    config('CONSUMER_SECRET'), 
    config('ACCESS_TOKEN_KEY'), 
    config('ACCESS_TOKEN_SECRET')
)

def getTweet(query):
    url = 'https://api.Twitter.com/1.1/search/tweets.json' ### url to Twitter JSON
    pms = {'q' : query, 'count' : 100, 'lang' : 'it', 'result_type': 'recent'} ### parameters according to Twitter API
    res = requests.get(url, params = pms, auth=auth)
    tweets = res.json()
    allTweets = []

    stop = 0
    count = 0

    while(stop == 0):
        StatusTweet = tweets.get('statuses')

        if not StatusTweet:
            break
            
        allTweets.append(tuple((StatusTweet[count].get('text'), StatusTweet[count].get('created_at'))))

        count = count + 1

        if(count == 10):
            break

    print(len(allTweets))
    return allTweets