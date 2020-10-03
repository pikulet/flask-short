from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy

def create_app():
     app = Flask(__name__)
     app.config.from_object(Config)
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
     Bootstrap(app)
     return app

app = create_app()
db = SQLAlchemy(app)

SHORTENED_LENGTH = 6

from app import routes
