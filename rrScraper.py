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
soup = bs(page.content, 'html.parser')

results = soup.find_all('tr', class_='chapter-row')
#print text version of results
#print(results)


#search for links to all chapters
urls = []
for result in results:
    chapter_url = result.find('a')['href']
    urls.append("http://royalroad.com"+chapter_url)

for url1 in urls:
    chapNum = str(urls.index(url1))
    chapter_page = requests.get(url1)
    chapter_soup = bs(chapter_page.content, 'html.parser')
    chapter_text = chapter_soup.find_all("span", attrs={"style":"font-size: 1.3em"})
    chapter_text_clean = []
    for text in chapter_text:
        chapter_text_clean.append(text.text.strip())
    chapter = epub.EpubHtml(title='Chapter '+ chapNum, file_name='chapter.xhtml', lang='en')
    chapter.content = chapter_text
    book.add_item(chapter)
    book.spine.append(chapter)

#search for all chapters
for result in results:
    #get chapter title
    #chapter_title = result.find(class_ = "chapter-title").get_text()
    #get chapter text
    #chapter_text = result.find(class_ = "chapter-text").get_text()
    #create chapter
    #chapter = epub.EpubHtml(title=chapter_title, file_name=chapter_title)
    #chapter.content = chapter_text
    pass
    #book.add_item(chapter)
    #book.toc.append(epub.Link(chapter_title, chapter_title, chapter_title))
    #book.spine.append(chapter)

#add NCX and nav
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

#writing the book
epub.write_epub('test.epub', book, {})