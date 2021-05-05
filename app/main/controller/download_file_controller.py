from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
from app import db
from app.main.controller import bp
from flask import Flask
#from app import app
from flask import Flask, send_file, render_template
from app.main.service.make_file_csv_service import lich_su_gia_co_phieu
from app.main.service.make_file_csv_service import kinh_doanh_theo_quy, kinh_doanh_theo_nam, can_doi_kt_theo_quy, can_doi_kt_theo_nam, lc_theo_quy, lc_theo_nam
from app.main.service.make_file_csv_service import lich_chia_co_tuc
from app.main.service.make_file_csv_service import tai_san, nguon_von, tien_mat_tren_co_phieu, ket_qua_kinh_doanh_quy, co_cau_loi_nhuan, cpqh_qldn_dt, pe_eps, roa_roe
from config.config import configs
const path = require('path');
config = configs()

@bp.route('/download/<ma_co_phieu1>', methods = ['GET', 'POST'])
def download(ma_co_phieu1):
    ma_co_phieu1 = request.form.get('code_co_phieu')
    return render_template('download.html', ma_co_phieu1=ma_co_phieu1, cache_timeout=0)


@bp.route('/download_file/<ma_co_phieu1>/download_lsgcp', methods = ['GET', 'POST'])
def lich_su_gia_co_phieu_1(ma_co_phieu1):
    url_file = lich_su_gia_co_phieu(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)



# NHIÊM VỤ 2

@bp.route('/download_file/<ma_co_phieu1>/download_kqkdtq', methods = ['GET', 'POST'])
def kinh_doanh_theo_quy_route(ma_co_phieu1):
    url_file = kinh_doanh_theo_quy(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>//download_kqkdtn', methods = ['GET', 'POST'])
def kinh_doanh_theo_nam_route(ma_co_phieu1):
    url_file = kinh_doanh_theo_nam(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>//download_cdkttq', methods = ['GET', 'POST'])
def can_doi_kt_theo_quy_route(ma_co_phieu1):
    url_file = can_doi_kt_theo_quy(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>//download_cdkttn', methods = ['GET', 'POST'])
def can_doi_kt_theo_nam_route(ma_co_phieu1):
    url_file = can_doi_kt_theo_nam(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_lctq', methods = ['GET', 'POST'])
def lc_theo_quy_route(ma_co_phieu1):
    url_file = lc_theo_quy(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_lctn', methods = ['GET', 'POST'])
def lc_theo_nam_route(ma_co_phieu1):
    url_file = lc_theo_nam(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

# NHIỆM VỤ 3

@bp.route('/download_file/<ma_co_phieu1>/download_lcct', methods = ['GET', 'POST'])
def lich_chia_co_tuc_route(ma_co_phieu1):
    url_file = lich_chia_co_tuc(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)
# NHIỆM VỤ 4
@bp.route('/download_file/<ma_co_phieu1>/download_ts', methods = ['GET', 'POST'])
def tai_san_route(ma_co_phieu1):
    url_file = tai_san(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_nv', methods = ['GET', 'POST'])
def nguon_von_route(ma_co_phieu1):
    url_file = nguon_von(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_tmtcp', methods = ['GET', 'POST'])
def tien_mat_tren_co_phieu_route(ma_co_phieu1):
    url_file = tien_mat_tren_co_phieu(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_kqkdq', methods = ['GET', 'POST'])
def ket_qua_kinh_doanh_quy_route(ma_co_phieu1):
    url_file = ket_qua_kinh_doanh_quy(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_ccln', methods = ['GET', 'POST'])
def co_cau_loi_nhuan_route(ma_co_phieu1):
    url_file = co_cau_loi_nhuan(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_cpqh_qldn_dt', methods = ['GET', 'POST'])
def cpqh_qldn_dt_route(ma_co_phieu1):
    url_file = cpqh_qldn_dt(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_pe_eps', methods = ['GET', 'POST'])
def pe_eps_route(ma_co_phieu1):
    url_file = pe_eps(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)

@bp.route('/download_file/<ma_co_phieu1>/download_roa_roe', methods = ['GET', 'POST'])
def roa_roe_route(ma_co_phieu1):
    url_file = roa_roe(ma_co_phieu1)
    path = r"..\\{0}".format(url_file)
    return send_file(path, as_attachment=True, cache_timeout=0)
