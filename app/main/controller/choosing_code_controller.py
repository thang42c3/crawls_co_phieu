from flask import render_template
from app.main.controller import bp
from app.main.model.code_of_stock import ma_co_phieus


@bp.route('/', methods = ['GET', 'POST'])
@bp.route('/index', methods = ['GET', 'POST'])
def index():
    ma_co_phieu = ma_co_phieus.query.all()
    return render_template('index.html', ma_co_phieus = ma_co_phieu, cache_timeout=0)

