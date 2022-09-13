from flask import Flask
from config import BaseConfig
from flask_cors import CORS


app = Flask(__name__,template_folder="static/templates")
app.config.from_object(BaseConfig)
CORS(app)
from app import views