import json

from .crud import CRUD
from .models import Consulate, Country, VisaApplicationCenter, News, NewsDetails


def get_data(file_name: str):
    with open('data/' + file_name, 'r', encoding='utf8') as rf:
        return json.load(rf)


def parse_consulates():
    data = get_data('consulates_info.json')
    return [
        Consulate(
            address=consulate['address'],
            email=None,
            working_hours=consulate['working hours'],
            phone_number_1=consulate['phone'].split(',')[0],
            phone_number_2=consulate['phone'].split(',')[1] if
            len(consulate['phone'].split(',')) > 1 else None,
            country=CRUD.select_all(Country)[0]
        )
        for consulate in data]


def parse_visa_centers():
    data = get_data('visa_centers_info.json')
    return [
        VisaApplicationCenter(
            address=center['address'],
            email=None,
            apply_working_hours_1=center['opening_hours'][0]['day'] + ', ' + center['opening_hours'][0]['hours'],
            issue_working_hours_2=center['opening_hours'][1]['day'] + ', ' + center['opening_hours'][1]['hours'],
            phone_number=None,
            country=CRUD.select_all(Country)[0]
        )
        for center in data]


def parse_news():
    data = get_data('news_info.json')
    return [
        News(
            date=news['date'],
            country=CRUD.select_all(Country)[0],
            news_details=NewsDetails(None, news['news'], news['link'])
        )
        for news in data]


def create_country():
    CRUD.insert(Country(name='Poland'))


def create_consulates():
    consulates = parse_consulates()
    CRUD.insert_list(consulates)


def create_vise_centers():
    centers = parse_visa_centers()
    CRUD.insert_list(centers)


def create_news():
    news = parse_news()
    CRUD.insert_list(news)


def initialize_db():
    create_country()
    create_consulates()
    create_vise_centers()
    create_news()
