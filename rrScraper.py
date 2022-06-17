import requests
from bs4 import BeautifulSoup as bs

import ebooklib
from ebooklib import epub

book = epub.EpubBook()

#set book metadeta
book.set_identifier('id123456')
book.set_title('Sample book')
book.set_language('en')

book.add_author('Author')

url = "https://www.royalroad.com/fiction/22518/chrysalis"
page = requests.get(url)
cont = str(page.content)

soup = bs(page.content, 'html.parser')
results = soup.find_all(class_ = "text-right")
a = open('holder.txt', 'w')
for result in results:
    #link = row.find('a').get('href')
    print(result.get('href'))
    #print(result.text) #.text.strip()
    #a.write(result.text + '\n') #.text.strip()
a.close()

#now that we have the text, we can loop through all of the pages to compile the whole story
#we can do this by adding the chapter number to the end of the url
#we can then use the same code to get the text



#soup = bs(page.content, 'html.parser')
#results = soup.find_all("span", attrs={"style":"font-size: 1.3em"})

#a = open('holder.txt', 'w')
#for result in results:
    #print(result.text.strip())
    #a.write(result.text.strip() + '\n')
#a.close()