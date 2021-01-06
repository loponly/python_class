import requests
from bs4 import BeautifulSoup


class Unegui():
    # attribute
    base_url = 'https://www.unegui.mn'
    filename = 'unegui_ouput.csv'

    # init
    # with validation
    def __init__(self, sub_url):
        self.url = self.base_url + sub_url

    def saveToCsv(self, data):
        with open(self.filename, 'w') as f:
            f.write('title,desription,price\n')
            for line in data:

                f.write(','.join(list(line.values()))+'\n')

    @staticmethod
    def validate_string(text):
        if isinstance(text, str):
            return text
        return ''

    def get_content(self, soup):
        data = []
        for container in soup.select('div.list-announcement-block'):
            d = {}

            d['title'] = self.validate_string(container.select(
                'a.announcement-block__title')[0].attrs['content'])

            d['description'] = self.validate_string(container.select(
                'div[itemprop="description"]')[0].string)

            price = container.select('div.announcement-block__price')[0]
            d['price'] = self.validate_string(
                ' '.join(price.contents[0].split()))

            data.append(d)
        return data

    def request_get(self):
        response = requests.get(
            url=self.url,
            headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

        print(self.url, response.status_code)

        if response.status_code != 200:
            raise requests.exceptions.BaseHTTPError

        soup = BeautifulSoup(response.content, 'html.parser')

        return soup

    def run(self):
        link = True
        all_data = list()

        i = 0
        while link:
            soup = self.request_get()
            link = soup.select('a.number-list-next')

            all_data.extend(self.get_content(soup))

            self.url = f"{self.base_url}{link[0].attrs['href']}"
            break
            # i += 1
            # if i > 1:
            #     break
        return all_data

        # self.saveToCsv(all_data)


if __name__ == "__main__":
    for i, obj in enumerate([Unegui('/l-hdlh/l-hdlh-zarna/')]):
        obj.filename = f'output_{i}.csv'
        obj.run()
