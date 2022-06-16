from .es_crud import ES_CRUD
from . import scraper


def add_consulates_to_elasticsearch():
    consulates = scraper.get_consulates()
    for i in range(1, len(consulates) + 1):
        consulates[i-1]['id'] = i
        ES_CRUD.add_to_index('consulate', consulates[i-1])


def add_visa_centers_to_elasticsearch():
    visa_centers = scraper.get_visa_centers()
    for i in range(1, len(visa_centers) + 1):
        visa_centers[i-1]['id'] = i
        ES_CRUD.add_to_index('visaac', visa_centers[i-1])


def add_news_to_elasticsearch():
    all_news = scraper.get_news()

    for i in range(1, len(all_news) + 1):
        all_news[i-1]['id'] = i
        ES_CRUD.add_to_index('news', all_news[i-1])


def initialize_db():
    add_consulates_to_elasticsearch()
    add_visa_centers_to_elasticsearch()
    add_news_to_elasticsearch()
