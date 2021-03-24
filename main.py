from app import app
from flask import Flask, send_file, render_template
from scrapy import cmdline
from subprocess import Popen
from model.Model_NV_so_2 import kinh_doanh_theo_quy, kinh_doanh_theo_nam, can_doi_kt_theo_quy, can_doi_kt_theo_nam, lc_theo_quy, lc_theo_nam
from model.Model_NV_so_3 import lich_chia_co_tuc
from model.Model_NV_so_4 import tai_san, nguon_von, tien_mat_tren_co_phieu, ket_qua_kinh_doanh_quy, co_cau_loi_nhuan, cpqh_qldn_dt, pe_eps, roa_roe
import time

def run_NV_1():
    Popen('python model/Model_NV_so_1.py')

@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/download_lsgcp', methods = ['GET', 'POST'])
def lich_su_gia_co_phieu():
    run_NV_1()
    time.sleep(80)
    path = r".\file_csv\lich_su_gia_co_phieu.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

# NHIÊM VỤ 2

@app.route('/download_kqkdtq', methods = ['GET', 'POST'])
def kinh_doanh_theo_quy_route():
    kinh_doanh_theo_quy()
    path = r".\file_csv\kinh_doanh_theo_quy.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_kqkdtn', methods = ['GET', 'POST'])
def kinh_doanh_theo_nam_route():
    kinh_doanh_theo_nam()
    path = r".\file_csv\kinh_doanh_theo_nam.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_cdkttq', methods = ['GET', 'POST'])
def can_doi_kt_theo_quy_route():
    can_doi_kt_theo_quy()
    path = r".\file_csv\can_doi_kt_theo_quy.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_cdkttn', methods = ['GET', 'POST'])
def can_doi_kt_theo_nam_route():
    can_doi_kt_theo_nam()
    path = r".\file_csv\can_doi_kt_theo_nam.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_lctq', methods = ['GET', 'POST'])
def lc_theo_quy_route():
    lc_theo_quy()
    path = r".\file_csv\lc_theo_quy.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_lctn', methods = ['GET', 'POST'])
def lc_theo_nam_route():
    lc_theo_nam()
    path = r".\file_csv\lc_theo_nam.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

# NHIỆM VỤ 3

@app.route('/download_lcct', methods = ['GET', 'POST'])
def lich_chia_co_tuc_route():
    lich_chia_co_tuc()
    path = r".\file_csv\lich_chia_co_tuc.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)
# NHIỆM VỤ 4
@app.route('/download_ts', methods = ['GET', 'POST'])
def tai_san_route():
    tai_san()
    path = r".\file_csv\tai_san.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_nv', methods = ['GET', 'POST'])
def nguon_von_route():
    nguon_von()
    path = r".\file_csv\nguon_von.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_tmtcp', methods = ['GET', 'POST'])
def tien_mat_tren_co_phieu_route():
    tien_mat_tren_co_phieu()
    path = r".\file_csv\tien_mat_tren_co_phieu.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_kqkdq', methods = ['GET', 'POST'])
def ket_qua_kinh_doanh_quy_route():
    ket_qua_kinh_doanh_quy()
    path = r".\file_csv\ket_qua_kinh_doanh_quy.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_ccln', methods = ['GET', 'POST'])
def co_cau_loi_nhuan_route():
    co_cau_loi_nhuan()
    path = r".\file_csv\co_cau_loi_nhuan.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_cpqh_qldn_dt', methods = ['GET', 'POST'])
def cpqh_qldn_dt_route():
    cpqh_qldn_dt()
    path = r".\file_csv\cpqh_qldn_dt.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_pe_eps', methods = ['GET', 'POST'])
def pe_eps_route():
    pe_eps()
    path = r".\file_csv\pe_eps.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)

@app.route('/download_roa_roe', methods = ['GET', 'POST'])
def roa_roe_route():
    roa_roe()
    path = r".\file_csv\roa_roe.csv"
    return send_file(path, as_attachment=True, cache_timeout=0)



if __name__ == "__main__":
    app.run()