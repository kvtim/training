import os


class BaseConfig:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USERNAME = os.environ.get('USERNAME') or 'postgres'
    USER_PASSWORD = os.environ.get('USER_PASSWORD') or 'admin'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{USER_PASSWORD}@localhost/vfsdb'

    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.yaml'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
