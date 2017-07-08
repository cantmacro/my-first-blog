from django.apps import AppConfig



class NewsConfig(AppConfig):
    name = 'news'
def getnews():
    import requests
    url = 'https://newsapi.org/v1/articles?source=bild&sortBy=latest&apiKey='
    key = '7118812980574e7d9cb405ed88704034'
    url_final = url+key
    response = requests.get(url_final)
    status = response.status_code

    data = response.json()
    result = {}
    for i in data['articles']:

        for key,value in i.items():
            result[key] = result[value]

    return result
def sport1reader():
    import feedparser
    response = feedparser.parse('http://www.sport1.de/fussball/news.rss')
    data = response
    result = {}
    for z in data['entries']:
        result[z['id']]=z['summary']
    return result
def kickerreader():

    import feedparser
    response = feedparser.parse('http://rss.kicker.de/news/fussball')
    data = response
    result = {}
    for z in data['items']:
        result[z['id']] = z['summary']
    return result
