from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    app.config['SWAGGER_URL'],
    app.config['API_URL'],
    config={
        'app_name': 'polish api'
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=app.config['SWAGGER_URL'])

db = SQLAlchemy(app)

from . import routes
