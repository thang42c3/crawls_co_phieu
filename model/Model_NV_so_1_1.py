from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy import cmdline
import csv
import os
from subprocess import Popen
import logging
from Config import config
import json
from model.ghi_file import ghi_file

config = config()
logging.warning(config["url"]['lich_su_gia_co_phieu'])
logging.warning(config["url"]['tai_san'])
logging.warning(config["file_csv_url"]["lich_su_gia_co_phieu_bo_sung"])

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
    links = soup.find_all('tr')[6:]
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

    ghi_file(url_csv_file, rows)

    with open(r'{0}'.format(url_csv_file_bs), 'a') as f:
        write = csv.writer(f)
        write.writerow(fields)

    if os.path.exists(r'{0}'.format(url_csv_file_bs)):
        os.remove(r'{0}'.format(url_csv_file_bs))

    with open(r'{0}'.format(url_csv_file_bs), 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)

    with open(r'{0}'.format(url_csv_file), encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        data1 = list(reader)

    f.close()

    with open(r'{0}'.format(url_csv_file_bs), encoding='utf-8', newline='') as f:
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

    ghi_file(url_csv_file, data1)

