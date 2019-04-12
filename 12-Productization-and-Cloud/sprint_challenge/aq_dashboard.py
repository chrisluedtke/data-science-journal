"""OpenAQ Air Quality Dashboard with Flask."""
import json
from os import getenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .openaq import OpenAQ
from dotenv import load_dotenv

API = OpenAQ()
load_dotenv()

class Config(object):
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = getenv('FLASK_ENV')

APP = Flask(__name__)
APP.config.from_object(Config)
DB = SQLAlchemy(APP)

class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f"<Record {self.id} -- {self.datetime} -- {self.value}>"


def api_pull():
    _, body = API.measurements(city='Los Angeles', parameter='pm25')
    date_vals = []
    for result in body['results']:
        date = result['date']['utc']
        val = result['value']
        date_vals.append((date, val))

    return date_vals

@APP.shell_context_processor
def make_shell_context():
    return {'DB': DB, 'Record': Record}

@APP.route('/')
def root():
    """Base view."""
    data = Record.query.filter(Record.value >= 10).all()
    return str([(record.datetime, record.value) for record in data])

@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    data = api_pull()
    for datetime, value in data:
        record = Record(datetime=datetime, value=value)
        DB.session.add(record)
    DB.session.commit()
    
    return 'Data refreshed!'
