import json

from .crud import CRUD
from .es_crud import ES_CRUD
from .models import Consulate, Country, VisaApplicationCenter, News, NewsDetails


def get_data(file_name: str):
    with open('data/' + file_name, 'r', encoding='utf8') as rf:
        return json.load(rf)


def parse_consulates():
    data = get_data('consulates_info.json')
    return [
        {
            'address': consulate['address'],
            'email': None,
            'working_hours': consulate['working hours'],
            'phone_number_1': consulate['phone'].split(',')[0],
            'phone_number_2': consulate['phone'].split(',')[1] if
            len(consulate['phone'].split(',')) > 1 else None,
            'country': 'Poland'
        }
        for consulate in data]


def parse_visa_centers():
    data = get_data('visa_centers_info.json')
    return [
        {
            'address': center['address'],
            'email': None,
            'apply_working_hours_1': center['opening_hours'][0]['day'] + ', ' + center['opening_hours'][0]['hours'],
            'issue_working_hours_2': center['opening_hours'][1]['day'] + ', ' + center['opening_hours'][1]['hours'],
            'phone_number': None,
            'country': 'Poland'
        }
        for center in data]


def parse_news():
    data = get_data('news_info.json')
    return [
        {
            'date': news['date'],
            'country': 'Poland',
            'news_details': {
                'title': news['news'][:50],
                'body': news['news'],
                'link': news['link']
            }
        }
        for news in data]


def create_country():
    if CRUD.select_by_name(Country, 'Poland') is None:
        CRUD.insert(Country(name='Poland'))


def create_consulates():
    new_consulates = parse_consulates()

    old_consulates = CRUD.select_all(Consulate)

    for old in old_consulates:
        exists = False
        for new in new_consulates:
            if old.address == new['address']:
                exists = True
                if old != new:
                    CRUD.update(Consulate, old.id,
                                email=new['email'],
                                working_hours=new['working_hours'],
                                phone_number_1=new['phone_number_1'],
                                phone_number_2=new['phone_number_2'])

        if exists is False:
            CRUD.delete(old)

    consulates = [
        Consulate(
            address=new['address'],
            email=new['email'],
            working_hours=new['working_hours'],
            phone_number_1=new['phone_number_1'],
            phone_number_2=new['phone_number_2'],
            country=CRUD.select_by_name(Country, new['country'])
        ) for new in new_consulates if new['address'] not in [
            old.address for old in old_consulates]]

    CRUD.insert_list(consulates)


def create_visa_centers():
    new_centers = parse_visa_centers()

    old_centers = CRUD.select_all(VisaApplicationCenter)

    for old in old_centers:
        exists = False
        for new in new_centers:
            if old.address == new['address']:
                exists = True
                if old != new:
                    CRUD.update(VisaApplicationCenter, old.id,
                                email=new['email'],
                                apply_working_hours_1=new['apply_working_hours_1'],
                                issue_working_hours_2=new['issue_working_hours_2'],
                                phone_number=new['phone_number'])

        if exists is False:
            CRUD.delete(old)

    centers = [
        VisaApplicationCenter(
            address=new['address'],
            email=new['email'],
            apply_working_hours_1=new['apply_working_hours_1'],
            issue_working_hours_2=new['issue_working_hours_2'],
            phone_number=new['phone_number'],
            country=CRUD.select_by_name(Country, new['country'])
        ) for new in new_centers if new['address'] not in [
            old.address for old in old_centers]]

    CRUD.insert_list(centers)


def create_news():
    new_news = parse_news()

    old_news = CRUD.select_all(News)

    for old in old_news:
        exists = False
        for new in new_news:
            if old.news_details.link == new['news_details']['link']:
                exists = True
                if old != new:
                    CRUD.update(News, old.id,
                                date=new['date'])
                    CRUD.update(NewsDetails, old.news_details.id,
                                title=new['news_details']['title'],
                                body=new['news_details']['title'],
                                link=new['news_details']['link'])
        if exists is False:
            CRUD.delete(old)

    news = [
        News(
            date=new['date'],
            country=CRUD.select_by_name(Country, new['country']),
            news_details=NewsDetails(
                title=new['news_details']['title'],
                body=new['news_details']['body'],
                link=new['news_details']['link']
            )
        ) for new in new_news if new['news_details']['link'] not in [
            old.news_details.link for old in old_news]]

    CRUD.insert_list(news)


def add_consulates_to_elasticsearch():
    consulates = CRUD.select_all(Consulate)
    for consulate in consulates:
        ES_CRUD.add_to_index('consulate', {
            {
                'id': consulate.id,
                'address': consulate.address,
                'email': consulate.email,
                'working_hours': consulate.working_hours,
                'phone_number_1': consulate.phone_number_1,
                'phone_number_2': consulate.phone_number_2,
                'country': consulate.country.name
            }
        })


def add_visa_centers_to_elasticsearch():
    visa_centers = CRUD.select_all(VisaApplicationCenter)
    for center in visa_centers:
        ES_CRUD.add_to_index('visaac', {
            {
                'id': center.id,
                'address': center.address,
                'email': center.email,
                'apply_working_hours_1': center.apply_working_hours_1,
                'issue_working_hours_2': center.issue_working_hours_2,
                'phone_number': center.phone_number,
                'country': center.country.name
            }
        })


def add_news_to_elasticsearch():
    all_news = CRUD.select_all(News)
    for news in all_news:
        ES_CRUD.add_to_index('news', {
            {
                'id': news.id,
                'date': news.date,
                'title': news.news_details.title,
                'body': news.news_details.body,
                'link': news.news_details.link
            }
        })


def initialize_db():
    create_country()
    create_consulates()
    create_visa_centers()
    create_news()

    add_consulates_to_elasticsearch()
    add_visa_centers_to_elasticsearch()
    add_news_to_elasticsearch()
