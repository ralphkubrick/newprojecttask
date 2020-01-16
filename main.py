from bs4 import BeautifulSoup
from urllib import request

url = r'https://www.bbc.co.uk/news'
req = requests.Request(url)

with request.urlopen(req) as r:
    soup = r.read()

title = soup.title.string
print(title)
