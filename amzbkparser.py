#!/usr/bin/env python3

__version__ = '0.1'

import requests
from bs4 import BeautifulSoup as BS

def parse(url):
    headers = {'user-agent': 'Chrome/41.0.2228.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError('ERROR')

    soup = BS(response.content, 'html.parser')

    title = soup.find_all(id="productTitle")[0].string
    print(title)

    authors = soup.find_all('span', {'class':"author notFaded"})
    author_names = []

    for author in authors:
        name = author.find_all('a', {'class':'a-link-normal contributorNameID'})
        if name != []:
            author_names.append(name[0].string)

    print(author_names)

    img_url = soup.find_all(id='imgBlkFront')[0].get('src')
    print(img_url)

    details = soup.find_all('div', {'class':'content'})[0].ul.find_all('li')
    for item in details:
            if 'Publisher:' in item.text:
                        print(item.text)
                        publisher = item.text




def test():
    url = 'https://www.amazon.com/Ordinary-Differential-Equations-Dover-Mathematics/dp/0486649407/ref=sr_1_1?ie=UTF8&qid=1474146791&sr=8-1&keywords=ordinary+equation'
    parse(url)

if __name__ == '__main__':
    test()
