import os
import requests
import json
import csv
import os

# Crawl bảng lịch chia cổ tức VNM

def lich_chia_co_tuc():
    url = "https://api-finance-t19.24hmoney.vn/v1/ios/company/dividend-schedule?device_id=web&device_name=INVALID&device_model=Windows+10&network_carrier=INVALID&connection_type=INVALID&os=Chrome&os_version=89.0.4389.90&app_version=INVALID&access_token=INVALID&push_token=INVALID&locale=vi&symbol=VNM"
    proxies = {}
    response = requests.get(url = url, proxies=proxies)
    data = json.loads(response.content)

    if os.path.exists(r'.\file_csv\lich_chia_co_tuc.csv'):
        os.remove(r'.\file_csv\lich_chia_co_tuc.csv')
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

    with open(r'.\file_csv\lich_chia_co_tuc.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)

lich_chia_co_tuc()