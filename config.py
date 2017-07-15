import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# -- Flask
DEBUG = True
SECRET_KEY = "development_key"
CACHE_TIMEOUT = 60 * 60 * 15
APP_NAME = "Talk about flask"

# -- SQLAlchemy
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = True
