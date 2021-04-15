import os
import requests
import json
import csv
import os
from config import config
from model.ghi_file import ghi_file

config = config()


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

    ghi_file(url_csv_file, rows)
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

    ghi_file(url_csv_file, rows)
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

    ghi_file(url_csv_file, rows)
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

    ghi_file(url_csv_file, rows)
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
    ghi_file(url_csv_file, rows)
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
    ghi_file(url_csv_file, rows)
    return url_csv_file
