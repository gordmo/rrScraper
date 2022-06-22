import requests
from bs4 import BeautifulSoup as bs

import ebooklib
from ebooklib import epub

book = epub.EpubBook()

#set book metadeta (will parse for author and other metadata later)
book.set_identifier('id123456')
book.set_title('Sample book')
book.set_language('en')
book.add_author('Author')

#grabbing page full of chapters
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





#soup = bs(page.content, 'html.parser')
#results = soup.find_all("span", attrs={"style":"font-size: 1.3em"})

#a = open('holder.txt', 'w')
#for result in results:
    #print(result.text.strip())
    #a.write(result.text.strip() + '\n')
#a.close()

#create content before adding to book
c1 = epub.EpubHtml(title='introTest',
                    file_name='introTest.xhtml',
                    lang='en')
c1.set_content(u'<html><body><h1>Introduction</h1><p>Introduction paragraph.</p></body></html>')


c2 = epub.EpubHtml(title='About this book',
                   file_name='about.xhtml')
c2.set_content('<h1>About this book</h1><p>This is a book.</p>')

#adding content to the book
book.add_item(c1)
book.add_item(c2)
#technically this could hold any number of things (style sheets, images, html)

style = 'body { font-family: Times, Times New Roman, serif; }'
nav_css = epub.EpubItem(uid="style_nav",
                        file_name="style/nav.css",
                        media_type="text/css",
                        content=style)
book.add_item(nav_css)

#table of contents
book.toc = (epub.Link("introTest.xhtml", "introTest", 'intro'),
            (
                epub.Section("Languages"),
                (c1, c2)
            )
)

#creating the spine
book.spine = ['nav', c1, c2]

#add NCX and nav
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

#writing the book
epub.write_epub('test.epub', book, {})