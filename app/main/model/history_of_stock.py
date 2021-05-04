from flask import request
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField, TextAreaField
#from wtforms.validators import ValidationError, DataRequired, Length
#from flask_babel import _, lazy_gettext as _l
import scrapy
from scrapy import cmdline
from app import db
from app import create_app
app = create_app()
app.app_context().push()

import logging
logging.basicConfig(level=logging.DEBUG)



class history_of_stock(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    Ma_cty = db.Column(db.String(10))
    Ngay = db.Column(db.String(30))
    Gia_tham_chieu = db.Column(db.String(30))
    Len_xuong = db.Column(db.String(30))
    Phan_tram = db.Column(db.String(30))
    Dong_cua = db.Column(db.String(30))
    Khoi_luong = db.Column(db.String(30))
    Mo_cua = db.Column(db.String(30))
    Cao_nhat = db.Column(db.String(30))
    Thap_nhat = db.Column(db.String(30))
    Giao_dich = db.Column(db.String(30))
    Thoa_thuan = db.Column(db.String(30))
    Nuoc_ngoai_mua = db.Column(db.String(30))
    Nuoc_ngoai_ban = db.Column(db.String(30))

def __init__(self, name, code):
     self.name = name
     self.code = code

#db.metadata.clear()
#db.create_all()