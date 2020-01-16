from bs4 import BeautifulSoup
import requests

url = r'https://www.bbc.co.uk/news'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.title.string
print(title)
