import json
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def get_data(file_name: str):
    with open(file_name, 'r', encoding='utf8') as rf:
        return jsonify(json.load(rf))


@app.route("/api/consulates")
def get_consulates():
    return get_data('consulates_info.json')


@app.route("/api/vc")
def get_visa_canters():
    return get_data('visa_centers_info.json')


@app.route("/api/news")
def get_news():
    return get_data('news_info.json')


@app.route("/api/vc_and_consulates")
def get_visa_canters_and_consulates():
    return get_data('visa_centers_and_consulates_info.json')


@app.route("/api/all_data")
def get_all_data():
    return get_data('full_info.json')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
