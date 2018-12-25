import requests

result = requests.get('http://quotes.toscrape.com/')
page = result.text

