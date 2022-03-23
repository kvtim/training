import json
import os
import sqlite3
import time
import httpagentparser

from flask import Flask, redirect, request, url_for, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from oauthlib.oauth2 import WebApplicationClient
import requests

from db import init_db_command
from user import User

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)
print('hello, world')

try:
    init_db_command()
except sqlite3.OperationalError:
    pass  # Assume it's already been created

client = WebApplicationClient(GOOGLE_CLIENT_ID)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@app.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    login_user(user)

    return redirect(url_for("about"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template('about.html', name=current_user.name, email=current_user.email,
                           picture=current_user.profile_pic)


@app.route("/list/<city>")
def weather_for_7_days(city):

    weather_data = get_weather_data(city)

    return render_template('weather_for_7_days.html', days=weather_data[0], nights=weather_data[1], descr=weather_data[2],
                           unix_date=weather_data[3], date=weather_data[4], len=len(weather_data[0]), city=city)


@app.route("/get_weather", methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        city = request.form['city']
        return redirect(url_for('weather_for_7_days', city=city))

    return render_template('get_weather.html')


@app.route("/<city>/<date>")
def one_day_weather(city, date):
    weather_data = get_weather_data(city)
    day = weather_data[3].index(int(date))
    return render_template('one_day_weather.html', day=weather_data[0][day], night=weather_data[1][day],
                           descr=weather_data[2][day], date=weather_data[4][day], wind_speed=weather_data[5][day],
                           min_temp=weather_data[6][day], max_temp=weather_data[7][day], humidity=weather_data[8][day],
                           city=city)


@app.route("/useragent")
def useragent():
    ua = request.headers.get('User-Agent')
    info = httpagentparser.simple_detect(ua)
    return render_template('useragent.html', os=info[0], browser=info[1])


def get_weather_data(city):
    api_key = 'f0206eb326141b0726c72f9b73fe7e49'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    resp = requests.get(url)

    data = resp.json()

    lon = data['coord']['lon']
    lat = data['coord']['lat']

    exclude = 'minute,hourly'
    url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}&units=metric'

    resp2 = requests.get(url2)
    data_8_days = resp2.json()

    days = []
    nights = []
    descr = []
    unix_date = []
    wind_speed = []
    min_temp = []
    max_temp = []
    humidity = []

    for day in data_8_days['daily']:
        days.append(round(day['temp']['day']))

        nights.append(round(day['temp']['night']))

        descr.append(day['weather'][0]['main'] + ': ' + day['weather'][0]['description'])

        unix_date.append(day['dt'])

        wind_speed.append(day['wind_speed'])

        min_temp.append(round(day['temp']['min']))

        max_temp.append(round(day['temp']['max']))

        humidity.append(day['humidity'])

    date = list(map(lambda x: time.strftime('%Y-%m-%d', time.localtime(x)), unix_date))

    return [days, nights, descr, unix_date, date, wind_speed, min_temp, max_temp, humidity]


if __name__ == "__main__":
    app.run(ssl_context='adhoc', debug=True)
