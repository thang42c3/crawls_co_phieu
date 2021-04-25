import json
import logging
import os
logging.basicConfig(level=logging.INFO)
basedir = os.path.abspath(os.path.dirname(__file__))
def config():
    with open('.\config.json', 'r') as f:
        config = json.load(f)
    f.close()
    return config

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
