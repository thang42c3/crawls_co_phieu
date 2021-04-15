from app import app
from flask import Flask, send_file, render_template
from scrapy import cmdline
from subprocess import Popen
from model.model import lich_su_gia_co_phieu
from model.model import kinh_doanh_theo_quy, kinh_doanh_theo_nam, can_doi_kt_theo_quy, can_doi_kt_theo_nam, lc_theo_quy, lc_theo_nam
from model.model import lich_chia_co_tuc
from model.model import tai_san, nguon_von, tien_mat_tren_co_phieu, ket_qua_kinh_doanh_quy, co_cau_loi_nhuan, cpqh_qldn_dt, pe_eps, roa_roe
import time
from config import config
config = config()


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/download_lsgcp', methods = ['GET', 'POST'])
def lich_su_gia_co_phieu_1():
    url_file = lich_su_gia_co_phieu()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

# NHIÊM VỤ 2

@app.route('/download_kqkdtq', methods = ['GET', 'POST'])
def kinh_doanh_theo_quy_route():
    url_file = kinh_doanh_theo_quy()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_kqkdtn', methods = ['GET', 'POST'])
def kinh_doanh_theo_nam_route():
    url_file = kinh_doanh_theo_nam()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_cdkttq', methods = ['GET', 'POST'])
def can_doi_kt_theo_quy_route():
    url_file = can_doi_kt_theo_quy()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_cdkttn', methods = ['GET', 'POST'])
def can_doi_kt_theo_nam_route():
    url_file = can_doi_kt_theo_nam()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_lctq', methods = ['GET', 'POST'])
def lc_theo_quy_route():
    url_file = lc_theo_quy()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_lctn', methods = ['GET', 'POST'])
def lc_theo_nam_route():
    url_file = lc_theo_nam()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

# NHIỆM VỤ 3

@app.route('/download_lcct', methods = ['GET', 'POST'])
def lich_chia_co_tuc_route():
    url_file = lich_chia_co_tuc()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)
# NHIỆM VỤ 4
@app.route('/download_ts', methods = ['GET', 'POST'])
def tai_san_route():
    url_file = tai_san()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_nv', methods = ['GET', 'POST'])
def nguon_von_route():
    url_file = nguon_von()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_tmtcp', methods = ['GET', 'POST'])
def tien_mat_tren_co_phieu_route():
    url_file = tien_mat_tren_co_phieu()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_kqkdq', methods = ['GET', 'POST'])
def ket_qua_kinh_doanh_quy_route():
    url_file = ket_qua_kinh_doanh_quy()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_ccln', methods = ['GET', 'POST'])
def co_cau_loi_nhuan_route():
    url_file = co_cau_loi_nhuan()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_cpqh_qldn_dt', methods = ['GET', 'POST'])
def cpqh_qldn_dt_route():
    url_file = cpqh_qldn_dt()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_pe_eps', methods = ['GET', 'POST'])
def pe_eps_route():
    url_file = pe_eps()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_roa_roe', methods = ['GET', 'POST'])
def roa_roe_route():
    url_file = roa_roe()
    path = r"{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)



if __name__ == "__main__":
    app.run()
