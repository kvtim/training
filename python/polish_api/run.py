import json

from flask import Flask, jsonify, make_response
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy

from models.consulate import Consulate
from models.country import Country

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost/vfsdb'

db = SQLAlchemy(app)


country = Country('Poland')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'polish api'
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


def get_data(file_name: str):
    try:
        with open('data/' + file_name, 'r', encoding='utf8') as rf:
            return json.load(rf)
    except FileNotFoundError:
        return make_response(
            jsonify(
                {"error": "data not found"}
            ),
            404
        )


def parse_consulates():
    data = get_data('consulates_info.json')
    return [
        Consulate(address=consulate['address'],
                  email = None,
                  working_hours=consulate['working hours'],
                  phone_number_1=consulate['phone'].split(',')[0],
                  phone_number_2=consulate['phone'].split(',')[1] if len(consulate['phone'].split(',')) > 1 else None,
                  country=country)
        for consulate in data ]


@app.route("/api/c")
def c():
    s = []
    for c in parse_consulates():
        s.append(c.address)

    return str(''.join(s))


@app.route("/api/consulates")
def get_consulates():
    return get_data('consulates_info.json')


@app.route("/api/vc")
def get_visa_centers():
    return get_data('visa_centers_info.json')


@app.route("/api/news")
def get_news():
    return get_data('news_info.json')


@app.route("/api/vc_and_consulates")
def get_visa_centers_and_consulates():
    return get_data('visa_centers_and_consulates_info.json')


@app.route("/api/all_data")
def get_all_data():
    return get_data('full_info.json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
