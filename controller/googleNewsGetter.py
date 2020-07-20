import requests
from decouple import config
from datetime import datetime

GOOGLE_API_KEY = config('GOOGLE_NEWS_KEY')
today = datetime.today().strftime('%Y-%m-%d')

def getNews(query):
    url = ('http://newsapi.org/v2/everything?'
       'q='+ query + '&'
       'from=' + today + '&'
       'sortBy=popularity&'
       'apiKey=' + GOOGLE_API_KEY)
    response = requests.get(url)
    gNews = response.json()
    allNews = []
    urls = []

    news = 0

    #Why with while prints even same news
    #and with for prints differents news??? WTF
    #while(news == 0):

    for news in range(10):
        StatusNews = gNews.get('articles')

        if not StatusNews:
            break

        allNews.append(tuple((StatusNews[news].get('title'), StatusNews[news].get('publishedAt'))))
        urls.append(StatusNews[news].get('url'))
        
    print(len(allNews))
    return allNews, urls
