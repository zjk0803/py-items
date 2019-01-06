import requests

result = requests.get('http://quotes.toscrape.com/')
page = result.text
from selenium import webdriver
driver = webriver.Chrome()
driver.get('http://quotes.toscrape.com/')
page = driver.page_source
