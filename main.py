import time
import schedule
import requests
import smtplib
from DailyNews.hello import my_api_key
from DailyNews.hello import receiver_email
from DailyNews.hello import sender_email
from DailyNews.hello import my_password

country = 'ca'


def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=general&apiKey={my_api_key}"
    news = requests.get(url)
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


def send_email(news_string, sender_email, receiver_email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, my_password)

        subject = 'Top News Today'
        message = f'Subject: {subject}\n\n{news_string}'

        server.sendmail(sender_email, receiver_email, message)
        print("Email sent!")

    except Exception as e:
        print(f'Error sending email: {e}')
    finally:
        server.quit()


def main():
    news = get_news()
    if news:
        send_email(news, sender_email, receiver_email)
    else:
        print('Failed to get the news')


schedule.every().day.at('08:00').do(main)

if __name__ == "__main__":
    main()

    while True:
        schedule.run_pending()
        time.sleep(60)
