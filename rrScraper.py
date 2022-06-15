import requests
from bs4 import BeautifulSoup as bs

url = "https://www.royalroad.com/fiction/22518/chrysalis/chapter/331662/the-furious-tiny-the-delectable-feast"
page = requests.get(url)
cont = str(page.content)

soup = bs(page.content, 'html.parser')
results = soup.find_all("span", attrs={"style":"font-size: 1.3em"})

a = open('holder.txt', 'w')
for result in results:
    print(result.text.strip())
    a.write(result.text.strip() + '\n')
a.close()

#now that we have the text, we can loop through all of the pages to compile the whole story
#we can do this by adding the chapter number to the end of the url
#we can then use the same code to get the text


