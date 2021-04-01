from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy import cmdline
import csv
import os
from subprocess import Popen
import logging

def lich_su_gia_co_phieu():
    if os.path.exists(r'.\file_csv\lich_su_gia_co_phieu_bo_sung.csv'):
        os.remove(r'.\file_csv\lich_su_gia_co_phieu_bo_sung.csv')
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
    with open(r'.\file_csv\lich_su_gia_co_phieu_bo_sung.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow(fields)

    req = requests.get('https://www.cophieu68.vn/historyprice.php?currentPage=1&id=pan', verify=False)
    soup = BeautifulSoup(req.text, 'html.parser')
    logging.info("OK")
    links = soup.find_all('tr')[7:]
    rows = []
    for link in links:
        tds = link.find_all('td')
        list = []
        if len(tds) > 3:
            for i in range(0,13):
                if i == 0:
                    list.append(tds[i].text.strip("\n"))
                    list.append('PAN')
                else:
                    list.append(tds[i].text.strip("\n"))
        else:
            continue
        rows.append(list)

    with open(r'.\file_csv\lich_su_gia_co_phieu_bo_sung.csv', 'a') as f:
        write = csv.writer(f)
        write.writerows(rows)


    with open(r'.\file_csv\lich_su_gia_co_phieu.csv', newline='') as f:
        reader = csv.reader(f)
        data1 = list(reader)

    f.close()

    with open(r'.\file_csv\lich_su_gia_co_phieu_bo_sung.csv', newline='') as f:
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
    print(data1)

    if os.path.exists(r'.\file_csv\lich_su_gia_co_phieu.csv'):
        os.remove(r'.\file_csv\lich_su_gia_co_phieu.csv')

    with open(r'.\file_csv\lich_su_gia_co_phieu.csv', 'a') as f:
        write = csv.writer(f)
        write.writerows(data1)
