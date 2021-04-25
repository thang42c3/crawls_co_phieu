from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
import scrapy
from scrapy import cmdline
from app import db
from app import create_app
#app = create_app()
#app.app_context().push()

import logging
logging.basicConfig(level=logging.DEBUG)



class ma_co_phieus(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(30))

def __init__(self, name, code):
     self.name = name
     self.code = code

#db.metadata.clear()
#db.create_all()