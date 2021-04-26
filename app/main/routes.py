from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db
from app.main import bp
from app.main.forms import ma_co_phieus
from flask import Flask

@bp.route('/')
@bp.route('/index')
def index():
    ma_co_phieu = ma_co_phieus.query.all()
    return render_template('index.html', ma_co_phieus = ma_co_phieu)

