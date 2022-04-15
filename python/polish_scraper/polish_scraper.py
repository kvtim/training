import json

from news_scraper import NewsScraper
from visa_centers_scraper import ViseCentersScraper
from consulates_scraper import ConsulatesScraper


class PolishScraper:
    def __init__(self, language='ru', dest_country='pol', country='blr'):
        self.visa_centers = ViseCentersScraper(language, dest_country, country)
        self.news = NewsScraper(language, dest_country, country)
        self.consulates = ConsulatesScraper()

    def get_full_json(self):
        info = {
            'visa centers info': self.visa_centers.get_data(),
            'news': self.news.get_data(),
            'consulates info': self.consulates.get_data()
        }
        with open('full_info.json', 'w', encoding='utf8') as wf:
            json.dump(info, wf, indent=4, ensure_ascii=False)

    def get_visa_centers_and_consulates_json(self):
        info = {
            'visa centers info': self.visa_centers.get_data(),
            'consulates info': self.consulates.get_data()
        }
        with open('visa_centers_and_consulates_info.json', 'w', encoding='utf8') as wf:
            json.dump(info, wf, indent=4, ensure_ascii=False)

    def get_visa_centers_json(self):
        with open('visa_centers_info.json', 'w', encoding='utf8') as wf:
            json.dump(self.visa_centers.get_data(), wf, indent=4, ensure_ascii=False)

    def get_news_json(self):
        with open('news_info.json', 'w', encoding='utf8') as wf:
            json.dump(self.news.get_data(), wf, indent=4, ensure_ascii=False)

    def get_consulates_json(self):
        with open('consulates_info.json', 'w', encoding='utf8') as wf:
            json.dump(self.consulates.get_data(), wf, indent=4, ensure_ascii=False)

scraper = PolishScraper()
scraper.get_consulates_json()
scraper.get_news_json()
scraper.get_visa_centers_json()
scraper.get_visa_centers_and_consulates_json()
scraper.get_full_json()
