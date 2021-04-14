import os
import requests
import json
import csv
import os
from model.ghi_file import ghi_file
from config import config
config = config()

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
    ghi_file(url_csv_file, rows)

