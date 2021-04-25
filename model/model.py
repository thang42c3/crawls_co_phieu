from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy import cmdline
import csv
import os
from subprocess import Popen
import logging
from config import config
import json
from model.save_file import save_file

config = config()

def lich_su_gia_co_phieu():
    url_csv_file = config["file_csv_url"]["lich_su_gia_co_phieu"]
    fields = ['STT',
              'Ma_cty',
              'Ngay',
              'Gia_tham_chieu',
              'Len_xuong',
              'Phan_tram',
              'Dong_cua',
              'Khoi_luong',
              'Mo_cua',
              'Cao_nhat',
              'Thap_nhat',
              'Giao_dich_thoa_thuan',
              'Nuoc_ngoai_mua',
              'Nuoc_ngoai_ban']


    req = requests.get(config["url"]['lich_su_gia_co_phieu'], verify=False)
    soup = BeautifulSoup(req.text, 'html.parser')
    links = soup.find_all('tr')[7:]
    rows = []
    rows.append(fields)
    for link in links:
        tds = link.find_all('td')
        lis = []
        if len(tds) > 3:
            for i in range(0,13):
                if i == 0:
                    lis.append(tds[i].text.strip("\n"))
                    lis.append('PAN')
                else:
                    lis.append(tds[i].text.strip("\n"))
        else:
            continue
        rows.append(lis)
    logging.warning(rows)

    save_file(url_csv_file, rows)
    return url_csv_file


# NHIỆM VỤ SỐ 2
# Crawl bảng kết quả kinh doanh theo quý
def kinh_doanh_theo_quy():
    url = config["url"]['kinh_doanh_theo_quy']
    url_csv_file = config["file_csv_url"]["kinh_doanh_theo_quy"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    # Dòng tiêu đề.
    Tieu_de = ['Tiêu đề']
    for d in data['data']['headers']:
        Percent_or_not = d['type']
        quarter = d['quarter']
        year = d['year']
        if Percent_or_not == 'normal':
            Tieu_de.append("Q{0}/{1}".format(quarter, year))
        else:
            Tieu_de.append("% Q{0}/{1}".format(quarter, year))

    # Các dòng dữ liệu
    rows = []
    rows.append(Tieu_de)
    for r in data['data']['rows']:
        row = []
        Colum1 = r['name']
        value = r['values']
        row.append(Colum1)
        row = row + value
        rows.append(row)

    save_file(url_csv_file, rows)
    return url_csv_file

# Crawl bảng kết quả kinh doanh theo năm

def kinh_doanh_theo_nam():
    url = config["url"]['kinh_doanh_theo_nam']
    url_csv_file = config["file_csv_url"]["kinh_doanh_theo_nam"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    # Dòng tiêu đề.
    Tieu_de = ['Tiêu đề']
    for d in data['data']['headers']:
        Percent_or_not = d['type']
        year = d['year']
        if Percent_or_not == 'normal':
            Tieu_de.append("{0}".format(year))
        else:
            Tieu_de.append("%{0}".format(year))
    # Các dòng dữ liệu
    rows = []
    rows.append(Tieu_de)
    for r in data['data']['rows']:
        row = []
        Colum1 = r['name']
        value = r['values']
        row.append(Colum1)
        row = row + value
        rows.append(row)

    save_file(url_csv_file, rows)
    return url_csv_file


# Crawl bảng can doi kinh phi theo quý

def can_doi_kt_theo_quy():
    url = config["url"]['can_doi_kt_theo_quy']
    url_csv_file = config["file_csv_url"]["can_doi_kt_theo_quy"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    # Dòng tiêu đề.
    Tieu_de = ['Tiêu đề']
    for d in data['data']['headers']:
        Percent_or_not = d['type']
        quarter = d['quarter']
        year = d['year']
        if Percent_or_not == 'normal':
            Tieu_de.append("Q{0}/{1}".format(quarter,year))
        else:
            Tieu_de.append("% Q{0}/{1}".format(quarter,year))
    # Các dòng dữ liệu
    rows = []
    rows.append(Tieu_de)
    for r in data['data']['rows']:
        row = []
        Colum1 = r['name']
        value = r['values']
        row.append(Colum1)
        row = row + value
        rows.append(row)

    save_file(url_csv_file, rows)
    return url_csv_file


# Crawl bảng can doi kinh phi theo năm

def can_doi_kt_theo_nam():
    url = config["url"]['can_doi_kt_theo_nam']
    url_csv_file = config["file_csv_url"]["can_doi_kt_theo_nam"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    # Dòng tiêu đề.
    Tieu_de = ['Tiêu đề']
    for d in data['data']['headers']:
        Percent_or_not = d['type']
        year = d['year']
        if Percent_or_not == 'normal':
            Tieu_de.append("{0}".format(year))
        else:
            Tieu_de.append("%{0}".format(year))
    # Các dòng dữ liệu
    rows = []
    rows.append(Tieu_de)

    for r in data['data']['rows']:
        row = []
        Colum1 = r['name']
        value = r['values']
        row.append(Colum1)
        row = row + value
        rows.append(row)

    save_file(url_csv_file, rows)
    return url_csv_file


# Crawl bảng LC tài chính theo quý
def lc_theo_quy():
    url = config["url"]['lc_theo_quy']
    url_csv_file = config["file_csv_url"]["lc_theo_quy"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    # Dòng tiêu đề.
    Tieu_de = ['Tiêu đề']
    for d in data['data']['headers']:
        Percent_or_not = d['type']
        quarter = d['quarter']
        year = d['year']
        if Percent_or_not == 'normal':
            Tieu_de.append("Q{0}/{1}".format(quarter,year))
        else:
            Tieu_de.append("% Q{0}/{1}".format(quarter,year))
    # Các dòng dữ liệu
    rows = []
    rows.append(Tieu_de)
    for r in data['data']['rows']:
        row = []
        Colum1 = r['name']
        value = r['values']
        row.append(Colum1)
        row = row + value
        rows.append(row)
    save_file(url_csv_file, rows)
    return url_csv_file


# Crawl bảng LC tài chính theo năm

def lc_theo_nam():
    url = config["url"]['lc_theo_nam']
    url_csv_file = config["file_csv_url"]["lc_theo_nam"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    # Dòng tiêu đề.
    Tieu_de = ['Tiêu đề']
    for d in data['data']['headers']:
        Percent_or_not = d['type']
        year = d['year']
        if Percent_or_not == 'normal':
            Tieu_de.append("{0}".format(year))
        else:
            Tieu_de.append("%{0}".format(year))
    # Các dòng dữ liệu
    rows = []
    rows.append(Tieu_de)

    for r in data['data']['rows']:
        row = []
        Colum1 = r['name']
        value = r['values']
        row.append(Colum1)
        row = row + value
        rows.append(row)
    save_file(url_csv_file, rows)
    return url_csv_file

# NHIỆM VỤ SỐ 3

# Crawl bảng lịch chia cổ tức VNM

def lich_chia_co_tuc():
    url = config["url"]['lich_chia_co_tuc']
    url_csv_file = config["file_csv_url"]["lich_chia_co_tuc"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'Thông tin'])

    for d in data['data']:
        thoi_gian = d['end_date']
        type = d['type']
        ratio = d['ratio']
        if type == 1:
            text = 'Cổ tức bằng tiền, tỷ lệ: {0} %'.format(ratio*100)
        elif type == 2:
            text = "Thưởng bằng cổ phiếu, tỷ lệ: 1: {0}".format(ratio)
        else:
            text = "Phát hành thêm cổ phiếu, tỷ lệ: 1 : {0}".format(ratio)

        rows.append([thoi_gian, text])
    save_file(url_csv_file, rows)
    return url_csv_file



# NHIỆM VỤ 4
# 1. Crawl bảng tài sản
def tai_san():
    url = config["url"]['lich_chia_co_tuc']
    url_csv_file = config["file_csv_url"]["lich_chia_co_tuc"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'Tiền + Gửi + NH', 'Tồn kho', 'Tổng phải thu', 'Tổng TSCĐ', 'Đầu tư TC', 'Tài sản khác', '% Tiền/TTS' ])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Tien_gui_NH = d['y']
        Ton_kho = d['y1']
        Tong_phai_thu = d['y2']
        Tong_TSCD = d['y3']
        Dau_tu_TC = d['y4']
        Tai_san_khac = d['y5']
        Phan_tram_tien_TTS = str(d['y6']) + " %"
        i = i +1
        rows.append([Thoi_gian, Tien_gui_NH, Ton_kho, Tong_phai_thu, Tong_TSCD, Dau_tu_TC, Tai_san_khac, Phan_tram_tien_TTS])
    save_file(url_csv_file, rows)
    return url_csv_file


# 2. Crawl bảng nguồn vốn

def nguon_von():
    url = config["url"]['nguon_von']
    url_csv_file = config["file_csv_url"]["nguon_von"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'Nợ vay/Nợ phải trả', 'Vốn góp', 'Thặng dư + quỹ', 'LNST chưa pp', '% Nợ vay/TTS'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        No_vay_no_phai_tra = d['y']
        Von_gop = d['y1']
        Thang_du_quy = d['y2']
        LNST_chua_pp = d['y3']
        Phan_tram_no_vay = d['y4']
        i = i +1
        rows.append([Thoi_gian, No_vay_no_phai_tra, Von_gop, Thang_du_quy, LNST_chua_pp, Phan_tram_no_vay])
    save_file(url_csv_file, rows)
    return url_csv_file


# 3. Crawl tiền mặt trên cổ phiếu
def tien_mat_tren_co_phieu():
    url = config["url"]['tien_mat_tren_co_phieu']
    url_csv_file = config["file_csv_url"]["tien_mat_tren_co_phieu"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'Giá CP điều chỉnh', 'Cash per share'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Gia_cp_dieu_chinh = d['y']
        Cash_per_share = d['y1']*1000
        i = i +1
        rows.append([Thoi_gian, Gia_cp_dieu_chinh, Cash_per_share])
    save_file(url_csv_file, rows)
    return url_csv_file


# 4. Kết quả kinh doanh quý
def ket_qua_kinh_doanh_quy():
    url = config["url"]['ket_qua_kinh_doanh_quy']
    url_csv_file = config["file_csv_url"]["ket_qua_kinh_doanh_quy"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'Doanh thu 4 quý gần nhất (tỷ)', 'LNST 4 quý gần nhất (tỷ)', 'Biên LN gộp (%)', 'Biên LN ròng (%)'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Doanh_thu_4_quy = d['y']
        LNST_4_quy = d['y1']
        Bien_LN_gop = d['y2']
        Bien_LN_rong = d['y3']
        i = i +1
        rows.append([Thoi_gian, Doanh_thu_4_quy, LNST_4_quy, Bien_LN_gop, Bien_LN_rong])
    save_file(url_csv_file, rows)
    return url_csv_file

# 5. Cơ cấu lợi nhuận

def co_cau_loi_nhuan():
    url = config["url"]['co_cau_loi_nhuan']
    url_csv_file = config["file_csv_url"]["co_cau_loi_nhuan"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'LN khác (tỷ)', 'Tổng LNKT trước thuế (tỷ)', 'Lãi/lỗ từ hoạt động kinh doanh (tỷ)', 'Tăng trưởng lợi nhuận cùng kỳ (%)'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        LN_khac = d['y']
        Tong_LNKT_truoc_thue = d['y1']
        Lai_lo = d['y2']
        Tang_truong_loi_nhuan = d['y3']
        i = i +1
        rows.append([Thoi_gian, LN_khac, Tong_LNKT_truoc_thue, Lai_lo, Tang_truong_loi_nhuan])
    save_file(url_csv_file, rows)
    return url_csv_file


# 6. CPQH + QLDN + DT

def cpqh_qldn_dt():
    url = config["url"]['cpqh_qldn_dt']
    url_csv_file = config["file_csv_url"]["cpqh_qldn_dt"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', '(CPBH+CPQL)/DTT 4QGN', '(CPBH+CPQL)/DTT Quý'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Cpbh_cpql_4qgn = d['y']
        Cpbh_cpql_quy = d['y1']
        i = i +1
        rows.append([Thoi_gian, Cpbh_cpql_4qgn, Cpbh_cpql_quy])
    print(rows)
    with open(r'.\file_csv\cpqh_qldn_dt.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    save_file(url_csv_file, rows)
    return url_csv_file



# 7. Đồ thị P/E, EPS pha loãng
def pe_eps():
    url = config["url"]['pe_eps']
    url_csv_file = config["file_csv_url"]["pe_eps"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'EPS pha loãng (đồng)', 'P/E (lần)'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Eps_pha_loang = d['y']
        P_e = d['y1']
        i = i +1
        rows.append([Thoi_gian, Eps_pha_loang, P_e])
    save_file(url_csv_file, rows)
    return url_csv_file



# 8. ROA-ROE
def roa_roe():
    url = config["url"]['roa_roe']
    url_csv_file = config["file_csv_url"]["roa_roe"]
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)
    rows = []
    rows.append(['Thời gian', 'ROA quý (%)', 'ROE quý (%)', 'ROA 4qgn (%)', 'ROE 4qgn (%)'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Roa_quy = d['y']
        Roe_quy = d['y1']
        Roa_4qgn = d['y2']
        Roe_4qgn = d['y3']
        i = i +1
        rows.append([Thoi_gian, Roa_quy, Roe_quy, Roa_4qgn,Roe_4qgn ])
    save_file(url_csv_file, rows)
    return url_csv_file


