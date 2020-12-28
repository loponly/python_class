import requests
from bs4 import BeautifulSoup
from pprint import pprint
# http request


def saveToCsv(data, filename='unegui_ouput.csv'):

    with open(filename, 'w') as f:
        f.write('title,desription,price\n')

        for line in data:
            f.write(','.join(list(line.values()))+'\n')


base_url = 'https://www.unegui.mn'


# 404 500 400 XSD XML HTML HTML5 CSS
# bootstrap


def get_content(soup):
    data = []
    for container in soup.select('div.list-announcement-block'):
        d = {}

        d['title'] = container.select(
            'a.announcement-block__title')[0].attrs['content']

        d['description'] = container.select(
            'div[itemprop="description"]')[0].string

        price = container.select('div.announcement-block__price')[0]
        d['price'] = ' '.join(price.contents[0].split())
        data.append(d)
    return data


response = requests.get(
    url='https://www.unegui.mn/l-hdlh/l-hdlh-zarna/',
    headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

soup = BeautifulSoup(response.content, 'html.parser')

link = soup.select('a.number-list-next')

all_data = []
i = 0

while link:
    import time
    response = requests.get(url=f"{base_url}{link[0].attrs['href']}")
    print(link[0].attrs['href'])
    soup = BeautifulSoup(response.content, 'html.parser')
    all_data.extend(get_content(soup))
    link = soup.select('a.number-list-next')
    i += 1
    if i > 10:
        break

saveToCsv(all_data)
