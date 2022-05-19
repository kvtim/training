import json

from app import app
from .crud import CRUD
from .models import Consulate, Country, VisaApplicationCenter, News, NewsDetails
from .utils import parse_consulates, find_consulates_updates


@app.route("/api/test")
def test():
    # insert data
    # CRUD.insert(Country(name='Poland'))
    # return CRUD.select_by_id(Country, 1).name

    # select data by id
    # country = CRUD.select_by_id(Country, 1)
    # return country

    # select all data
    # countries = CRUD.select_all(Country)
    # return countries[0].name

    # update
    # CRUD.update(Country, 1, name='Pl')
    # return CRUD.select_by_id(Country, 1).name

    # CRUD.update(Country, 1, name='Poland')
    # return CRUD.select_by_id(Country, 1).name

    # delete
    #  CRUD.delete(CRUD.select_by_id(Country, 2))
    # return 'deleted'

    # CRUD.insert(Country(name='Poland'))
    country = CRUD.select_by_name(Country, 'Poland')
    return country.name


@app.route("/api/consulates")
def get_consulates():
    consulates = CRUD.select_all(Consulate)

    results = {'consulates': [
        {'country': consulate.country.name,
         'address': consulate.address,
         'email': consulate.email,
         'working_hours': consulate.working_hours,
         'phone_number_1': consulate.phone_number_1,
         'phone_number_2': consulate.phone_number_2,
         } for consulate in consulates]
    }
    return results


@app.route("/api/vac")
def get_visa_centers():
    visa_centers = CRUD.select_all(VisaApplicationCenter)
    results = {'visa_centers': [
        {'country': visa_center.country.name,
         'address': visa_center.address,
         'email': visa_center.email,
         'apply_working_hours_1': visa_center.apply_working_hours_1,
         'issue_working_hours_1': visa_center.issue_working_hours_2,
         'phone_number': visa_center.phone_number
         } for visa_center in visa_centers]
    }
    return results


@app.route("/api/news")
def get_news():
    news = CRUD.select_all(News)
    results = {'news': [
        {'date': n.date,
         'country': n.country.name,
         'news_details': {
             'title': n.news_details.title,
             'body': n.news_details.body,
             'link': n.news_details.link}
         } for n in news]
    }
    return results


@app.route("/api/vac_and_consulates")
def get_visa_centers_and_consulates():
    results = {
        'visa centers info': get_visa_centers(),
        'consulates info': get_consulates()
    }
    return results


@app.route("/api/all_data")
def get_all_data():
    results = {
        'consulates info': get_consulates(),
        'news': get_news(),
        'visa centers info': get_visa_centers()
    }
    return results
