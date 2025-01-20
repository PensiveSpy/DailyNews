import time
import requests
import smtplib
from DailyNews.hello import my_api_key
from DailyNews.hello import receiver_email
from DailyNews.hello import sender_email

country = 'ca'
URL = f"https://newsapi.org/v2/top-headlines?country={country}&category=general&apiKey={my_api_key}"

def get_news():
    news = requests.get(URL)
    if news.status_code == 200:
        news_data = news.json()
        articles = news_data.get('articles', [])[:20]
        news_list = []
        for article in articles:
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            news_list.append(f"Title: {title}\nDescription: {description}\nURL: {url}\n\n")
        return ''.join(news_list)
    else:
        return 'Failed to fetch news.'

