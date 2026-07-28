import requests

query = input("What type of news are you interested in today? ")
api = '00dcdacd3adf48d78aabf9b089c1cdca'

url = f'https://newsapi.org/v2/everything?q={query}&from=2026-06-28&sortBy=publishedAt&apiKey={api}'

response = requests.get(url)


data = response.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1, article['title'], article['url'])
    print('\n******************************************\n')
    