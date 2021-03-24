import requests
import json
import scrapy
from scrapy import cmdline
import csv
import os


# NHIỆM VỤ 4
# 1. Crawl bảng tài sản
def tai_san():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=0"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\tai_san.csv"):
        os.remove(r".\file_csv\tai_san.csv")
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
    print(rows)
    with open(r'.\file_csv\tai_san.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    return rows

# 2. Crawl bảng nguồn vốn

def nguon_von():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=1"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\nguon_von.csv"):
        os.remove(r".\file_csv\nguon_von.csv")
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
    print(rows)
    with open(r'.\file_csv\nguon_von.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    return rows

# 3. Crawl tiền mặt trên cổ phiếu
def tien_mat_tren_co_phieu():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=2"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\tien_mat_tren_co_phieu.csv"):
        os.remove(r".\file_csv\tien_mat_tren_co_phieu.csv")
    rows = []
    rows.append(['Thời gian', 'Giá CP điều chỉnh', 'Cash per share'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Gia_cp_dieu_chinh = d['y']
        Cash_per_share = d['y1']*1000
        i = i +1
        rows.append([Thoi_gian, Gia_cp_dieu_chinh, Cash_per_share])
    print(rows)
    with open(r'.\file_csv\tien_mat_tren_co_phieu.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    return rows

# 4. Kết quả kinh doanh quý
def ket_qua_kinh_doanh_quy():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=3"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\ket_qua_kinh_doanh_quy.csv"):
        os.remove(r".\file_csv\ket_qua_kinh_doanh_quy.csv")
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
    print(rows)
    with open(r'.\file_csv\ket_qua_kinh_doanh_quy.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    return rows

# 5. Cơ cấu lợi nhuận

def co_cau_loi_nhuan():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=4"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\co_cau_loi_nhuan.csv"):
        os.remove(r".\file_csv\co_cau_loi_nhuan.csv")
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
    print(rows)
    with open(r'.\file_csv\co_cau_loi_nhuan.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    return rows

# 6. CPQH + QLDN + DT

def cpqh_qldn_dt():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=5"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\cpqh_qldn_dt.csv"):
        os.remove(r".\file_csv\cpqh_qldn_dt.csv")
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
    return rows


# 7. Đồ thị P/E, EPS pha loãng
def pe_eps():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=6"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\pe_eps.csv"):
        os.remove(r".\file_csv\pe_eps.csv")
    rows = []
    rows.append(['Thời gian', 'EPS pha loãng (đồng)', 'P/E (lần)'])
    i = 0
    for d in data['data']["points"]:
        Thoi_gian = data['data']['x-axis'][i]['name']
        Eps_pha_loang = d['y']
        P_e = d['y1']
        i = i +1
        rows.append([Thoi_gian, Eps_pha_loang, P_e])
    print(rows)
    with open(r'.\file_csv\pe_eps.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    return rows


# 8. ROA-ROE
def roa_roe():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/financial-graph?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM&graph_type=7"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r".\file_csv\roa_roe.csv"):
        os.remove(r".\file_csv\roa_roe.csv")
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
    print(rows)
    with open(r'.\file_csv\roa_roe.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
    return rows