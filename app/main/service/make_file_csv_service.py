from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy import cmdline
import csv
import os
from subprocess import Popen
import logging
from config.config import configs
import json


config = configs()
basedir = os.getcwd()


def save_file(url_csv_file, rows):
#    url_csv_file = os.path.join(basedir, 'url_csv_file')
    if os.path.exists(r'{0}'.format(url_csv_file)):
        os.remove(r'{0}'.format(url_csv_file))

    with open(r'{0}'.format(url_csv_file), 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)

def get_url(loai_so_lieu, ma_co_phieu):
    url = config["url"][loai_so_lieu].format(ma_co_phieu)
    url_csv_file = config["file_csv_url"][loai_so_lieu] + "_{0}".format(ma_co_phieu) + ".csv"
#    url_csv_file = os.path.join(basedir, "{0}".format(url_csv_file))
    url_csv_file = basedir + "{0}".format(url_csv_file)
    response = requests.get(url=url, proxies={'http': '', 'https': ''})
    data = json.loads(response.content)
    return url_csv_file, data


def lich_su_gia_co_phieu(ma_co_phieu1):
    url_csv_file_bo_sung = config["file_csv_url"]["lich_su_gia_co_phieu_bo_sung"] + "_{0}.csv".format(ma_co_phieu1)
    url_csv_file = config["file_csv_url"]["lich_su_gia_co_phieu"] + "_{0}.csv".format(ma_co_phieu1)
    if os.path.exists(r'{0}'.format(url_csv_file_bo_sung)):
        os.remove(r'{0}'.format(url_csv_file))
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
    with open(r'{0}'.format(url_csv_file_bo_sung), 'a') as f:
        write = csv.writer(f)
        write.writerow(fields)

    url_lich_su_gia_co_phieu = config["url"]['lich_su_gia_co_phieu'] + str(ma_co_phieu1)
    req = requests.get(url_lich_su_gia_co_phieu, verify=False)
    soup = BeautifulSoup(req.text, 'html.parser')
    links = soup.find_all('tr')[7:]
    rows = []
    for link in links:
        tds = link.find_all('td')
        lis = []
        if len(tds) > 3:
            for i in range(0,13):
                if i == 0:
                    lis.append(tds[i].text.strip("\n"))
                    lis.append(ma_co_phieu1)
                else:
                    lis.append(tds[i].text.strip("\n"))
        else:
            continue
        logging.warning(lis)
        rows.append(lis)

    with open(r'{0}'.format(url_csv_file_bo_sung), 'a') as f:
        write = csv.writer(f)
        write.writerows(rows)


    with open(r'{0}'.format(url_csv_file), newline='') as f:
        reader = csv.reader(f)
        data1 = list(reader)

    f.close()

    with open(r'{0}'.format(url_csv_file_bo_sung), newline='') as f:
        reader = csv.reader(f)
        data2 = list(reader)

    f.close()
    list1 =[]
    for i in range(0, len(data2)):
        if i % 2 == 0:
            list1.append(data1[i][2])

    listdata2 = []
    for i in range(0, len(data2)):
        if i % 2 == 0:
            print(data2[i][2])
            if data2[i][2] not in list1:
                listdata2.insert(0, data2[i][2])

    for j in range(0,len(listdata2)+2):
        data1.insert(j+2, data2[j+2])

    def remove_values_from_list(the_list, val):
       return [value for value in the_list if value != val]

    data1 = remove_values_from_list(data1, [])

    for i in range(1, len(data1)):
        data1[i][0] = '#{0}'.format(i)
    save_file(url_csv_file, data1)
    return url_csv_file


# PHIÊN BẢN TẤT CẢ DỮ LIỆU NẰM TRONG BẢNG
"""
    url_csv_file = config["file_csv_url"]["lich_su_gia_co_phieu"] + "-{0}.csv".format(ma_co_phieu1)
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

    url_lich_su_gia_co_phieu = config["url"]['lich_su_gia_co_phieu'] + str(ma_co_phieu1)
    req = requests.get(url_lich_su_gia_co_phieu, verify=False)
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
"""






# NHIỆM VỤ SỐ 2
# Crawl bảng kết quả kinh doanh theo quý
def kinh_doanh_theo_quy(ma_co_phieu1):
    # Dòng tiêu đề.
    url_csv_file, data = get_url("kinh_doanh_theo_quy",ma_co_phieu1)
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

def kinh_doanh_theo_nam(ma_co_phieu1):
    url_csv_file, data = get_url("kinh_doanh_theo_nam",ma_co_phieu1)
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

def can_doi_kt_theo_quy(ma_co_phieu1):
    url_csv_file, data = get_url("can_doi_kt_theo_quy",ma_co_phieu1)
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

def can_doi_kt_theo_nam(ma_co_phieu1):
    url_csv_file, data = get_url("can_doi_kt_theo_nam",ma_co_phieu1)
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
def lc_theo_quy(ma_co_phieu1):
    url_csv_file, data = get_url("lc_theo_quy",ma_co_phieu1)
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

def lc_theo_nam(ma_co_phieu1):
    url_csv_file, data = get_url("lc_theo_nam",ma_co_phieu1)
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

def lich_chia_co_tuc(ma_co_phieu1):
    url_csv_file, data = get_url("lich_chia_co_tuc",ma_co_phieu1)
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
def tai_san(ma_co_phieu1):
    url_csv_file, data = get_url("tai_san",ma_co_phieu1)
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

def nguon_von(ma_co_phieu1):
    url_csv_file, data = get_url("nguon_von",ma_co_phieu1)
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
def tien_mat_tren_co_phieu(ma_co_phieu1):
    url_csv_file, data = get_url("tien_mat_tren_co_phieu",ma_co_phieu1)
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
def ket_qua_kinh_doanh_quy(ma_co_phieu1):
    url_csv_file, data = get_url("ket_qua_kinh_doanh_quy",ma_co_phieu1)
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

def co_cau_loi_nhuan(ma_co_phieu1):
    url_csv_file, data = get_url("co_cau_loi_nhuan",ma_co_phieu1)
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

def cpqh_qldn_dt(ma_co_phieu1):
    url_csv_file, data = get_url("cpqh_qldn_dt",ma_co_phieu1)
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
def pe_eps(ma_co_phieu1):
    url_csv_file, data = get_url("pe_eps",ma_co_phieu1)
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
def roa_roe(ma_co_phieu1):
    url_csv_file, data = get_url("roa_roe",ma_co_phieu1)
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

