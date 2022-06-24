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
url = "https://www.royalroad.com/fiction/46901/the-last-orellen"
page = requests.get(url)
soup = bs(page.content, 'html.parser')

results = soup.find_all('tr', class_='chapter-row')
book.toc = ()
#search for links to all chapters
urls = []
for result in results:
    chapter_url = result.find('a')['href']
    urls.append("http://royalroad.com"+chapter_url)

for url1 in urls:
    chapNum = str(urls.index(url1))
    chapter_page = requests.get(url1)
    chapter_soup = bs(chapter_page.content, 'html.parser')
    chapter_name = chapter_soup.find('h1', class_='font-white').text
    
    #clean string of any non-alphanumeric characters
    chapter_name = chapter_name.replace(' ', '_')

    chapter_name = ''.join(ch for ch in chapter_name if ch.isalnum())
    chapter_cont = chapter_soup.find("div", class_="chapter-inner chapter-content")
    chapter_text = chapter_cont.find_all('p')

    chapter_text_clean = []
    for text in chapter_text:
        chapter_text_clean.append(text.text.strip())

    chapter = epub.EpubHtml(title=chapter_name, file_name=chapter_name+'.xhtml', lang='en')
    #chapter.set_content = (u'<html><body><h1>chapter_name</h1><p>chapter_text_clean</p></body></html>').replace('chapter_name', chapter_name).replace('chapter_text_clean', ' '.join(chapter_text_clean))
    chapter.set_content = (u'<html><body><h1>'+chapter_name+'</h1><p>'+' '.join(chapter_text_clean)+'</p></body></html>')
    book.add_item(chapter)
    book.spine.append(chapter)
    print("appended chapter: "+ chapter_name)

#add NCX and nav
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

#writing the book
epub.write_epub('TLO.epub', book, {})