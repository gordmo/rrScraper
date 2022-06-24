import requests
from bs4 import BeautifulSoup as bs

import ebooklib
from ebooklib import epub

url = "https://www.royalroad.com/fiction/22518/chrysalis/chapter/331658/bleary-days"
page = requests.get(url)
soup = bs(page.content, 'html.parser')

chapter = soup.find("div", class_="chapter-inner chapter-content")
results = chapter.find_all('p')

for result in results:
    print(result.text)
