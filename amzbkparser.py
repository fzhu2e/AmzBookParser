#!/usr/bin/env python3

__version__ = '0.1'

import requests
from bs4 import BeautifulSoup as BS

class AmzBook(object):

    def __init__(
        self,
        title='',
        authors=[],
        publisher='',
        img_url='',
        link_url='',
        category='',
        progress=0
    ):
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.img_url = img_url
        self.link_url = link_url
        self.category = category
        self.progress = progress

    def __str__(self):
        return str(self.authors) + '\n' + str(self.title) + '\n' + str(self.publisher) + '\n' + '\n' + str(self.img_url)

def parse(url, debug=False):

    headers = {'user-agent': 'Chrome/41.0.2228.0'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError('ERROR')

    soup = BS(response.content, 'html.parser')

    if soup.find_all(id='productTitle') == []:
        title = soup.find_all(id='ebooksProductTitle')[0].string
    else:
        title = soup.find_all(id="productTitle")[0].string

    if debug: print(title)

    authors = soup.find_all('span', {'class':"author notFaded"})
    author_names = []

    for author in authors:
        name = author.find_all('a', {'class':'a-link-normal contributorNameID'})
        if name == []:
            name = author.find_all('a', {'class':'a-link-normal'})
        if name != []:
            author_names.append(name[0].string)

    if debug: print(author_names)

    img_url = soup.find_all(id='imgBlkFront')[0].get('src')
    if debug: print(img_url)

    details = soup.find_all(id='detail-bullets')[0].ul.find_all('li')
    for item in details:
        if 'Publisher:' in item.text:

            publisher = item.text.replace('Publisher:',"").lstrip()
            if debug: print(publisher)


    # create book
    book = AmzBook()
    book.title = title
    book.authors = author_names
    book.publisher = publisher
    book.img_url = img_url
    book.link_url = url

    return book


def test():
    urls = []
    urls.append('https://www.amazon.com/Ordinary-Differential-Equations-Dover-Mathematics/dp/0486649407/ref=sr_1_1?ie=UTF8&qid=1474146791&sr=8-1&keywords=ordinary+equation')
    urls.append('https://www.amazon.com/Schaums-Outline-Mathematica-2ed-Outlines/dp/0071608281')

    books = []

    for url in urls:
        books.append(parse(url, debug=True))
        print('...........................')

    for book in books:
        print(book)

if __name__ == '__main__':
    test()
