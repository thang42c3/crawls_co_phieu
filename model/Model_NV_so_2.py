import os
import requests
import json
import csv
import os


# Crawl bảng kết quả kinh doanh theo quý
def kinh_doanh_theo_quy():
    url = "https://api-t19.24hmoney.vn/v1/ios/report/statement/VNM/finance?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&period=2&view=2&page=1&expanded=true"
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



    if os.path.exists(r".\file_csv\kinh_doanh_theo_quy.csv"):
        os.remove(r".\file_csv\kinh_doanh_theo_quy.csv")

    with open(r'.\file_csv\kinh_doanh_theo_quy.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)

# Crawl bảng kết quả kinh doanh theo năm

def kinh_doanh_theo_nam():
    url = "https://api-t19.24hmoney.vn/v1/ios/report/statement/VNM/finance?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&period=1&view=2&page=1&expanded=true"
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




    if os.path.exists(r".\file_csv\kinh_doanh_theo_nam.csv"):
        os.remove(r".\file_csv\kinh_doanh_theo_nam.csv")

    with open(r'.\file_csv\kinh_doanh_theo_nam.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)


# Crawl bảng can doi kinh phi theo quý

def can_doi_kt_theo_quy():
    url = "https://api-t19.24hmoney.vn/v1/ios/report/statement/VNM/finance?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&period=2&view=1&page=1&expanded=true"
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

    if os.path.exists(r".\file_csv\can_doi_kt_theo_quy.csv"):
        os.remove(r".\file_csv\can_doi_kt_theo_quy.csv")

    with open(r'.\file_csv\can_doi_kt_theo_quy.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)

# Crawl bảng can doi kinh phi theo năm

def can_doi_kt_theo_nam():
    url = "https://api-t19.24hmoney.vn/v1/ios/report/statement/VNM/finance?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&period=1&view=1&page=1&expanded=true"
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

    if os.path.exists(r".\file_csv\can_doi_kt_theo_nam.csv"):
        os.remove(r".\file_csv\can_doi_kt_theo_nam.csv")

    with open(r'.\file_csv\can_doi_kt_theo_nam.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)


# Crawl bảng LC tài chính theo quý
def lc_theo_quy():
    url = "https://api-t19.24hmoney.vn/v1/ios/report/statement/VNM/finance?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&period=2&view=3&page=1&expanded=true"
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


    if os.path.exists(r".\file_csv\lc_theo_quy.csv"):
        os.remove(r".\file_csv\lc_theo_quy.csv")

    with open(r'.\file_csv\lc_theo_quy.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)

# Crawl bảng LC tài chính theo năm

def lc_theo_nam():
    url = "https://api-t19.24hmoney.vn/v1/ios/report/statement/VNM/finance?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&period=1&view=3&page=1&expanded=true"
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

    if os.path.exists(r".\file_csv\lc_theo_nam.csv"):
        os.remove(r".\file_csv\lc_theo_nam.csv")

    with open(r'.\file_csv\lc_theo_nam.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)