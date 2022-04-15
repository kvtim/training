import json

from visa_centers_scraper import VisaCentersScraper
from news_scraper import NewsScraper


class Scraper:
    def __init__(self):
        self.visa_centers = VisaCentersScraper()
        self.news = NewsScraper()

    def get_full_json(self):
        info = {
            'visa centers info': self.visa_centers.parse_html(),
            'news': self.news.parse_html()
        }

        with open('full_info.json', 'w') as wf:
            json.dump(info, wf, indent=4)

    def get_visa_centers_json(self):
        with open('visa_centers_info.json', 'w') as wf:
            json.dump(self.visa_centers.parse_html(), wf, indent=4)

    def get_news_json(self):
        with open('news_info.json', 'w') as wf:
            json.dump(self.news.parse_html(), wf, indent=4)


scraper = Scraper()
scraper.get_full_json()

with open('full_info.json', 'r') as rf:
    text = json.load(rf)

print(text)
