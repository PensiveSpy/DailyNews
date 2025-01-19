import time
from DailyNews.hello import my_api_key

country = 'ca'

url = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=20&apiKey={my_api_key}'
