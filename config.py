import os
from datetime import timedelta
import string

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    UPLOAD_FOLDER = "app/static/img"
    PLACEHOLDER_NAME = 'placeholder.jpg'
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(50)
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    DATABASES_FOLDER = os.path.join(basedir,'databases')
    DB_ANIMAL = os.path.join(DATABASES_FOLDER,'animal.db')
    URL = "https://animalbackend.herokuapp.com/"
    URL_PIC = URL + "static/img/"
    JSON_AS_ASCII = False
    DEBUG = True
    AVAILABLE_SYMBOLS = string.ascii_letters + string.digits
    TOKEN_LENGTH = 32