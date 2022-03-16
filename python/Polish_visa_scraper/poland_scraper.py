import json

from visa_centers_scraper import VisaCentersScraper
from news_scraper import NewsScraper


class Scraper:
    def __init__(self):
        self.visa_centers_scraper = VisaCentersScraper()
        self.news_scraper = NewsScraper()

    def get_json(self):
        info = {
            'visa centers info': self.visa_centers_scraper.parse_html(),
            'news': self.news_scraper.parse_html()
        }

        with open('info.json', 'w') as wf:
            json.dump(info, wf, indent=4)


scraper = Scraper()
scraper.get_json()


with open('info.json', 'r') as rf:
    text = json.load(rf)

print(text)
