import json
import scrapy
from scrapy import cmdline
import csv
import os
from subprocess import Popen


# NHIỆM VỤ SỐ 1
if os.path.exists(r".\file_csv\lich_su_gia_co_phieu.csv"):
    os.remove(r".\file_csv\lich_su_gia_co_phieu.csv")
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

with open(r'.\file_csv\lich_su_gia_co_phieu.csv', 'a') as f:
    write = csv.writer(f)
    write.writerow(fields)


class CpSpider(scrapy.Spider):
    name = 'cp_item'
    start_urls = ['https://www.cophieu68.vn/historyprice.php?currentPage=1&id=pan']
    #for i in range(1, 72):
        #   start_urls.append('https://www.cophieu68.vn/historyprice.php?currentPage={0}&id={1}'.format(i, Ten_cty))
    def parse(self, response):
        rows = []
        rows.append(fields)
        for table in response.css('table.stock'):
            for j in range (2, 3):
                record = [ table.xpath('tr[{0}]/td[1]/text()'.format(j)).get(),
                    'PAN',
                    table.xpath('tr[{0}]/td[2]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[3]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[4]/span[1]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[5]/span[1]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[6]/span[1]/strong[1]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[7]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[8]/span[1]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[9]/span[1]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[10]/span[1]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[11]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[12]/text()'.format(j)).get(),
                    table.xpath('tr[{0}]/td[13]/text()'.format(j)).get()
            ]
                if record[0] is not None:
                    rows.append(record)
        


        with open(r'.\file_csv\lich_su_gia_co_phieu.csv', 'a') as f:
            write = csv.writer(f)
            write.writerows(rows)
      
cmdline.execute("scrapy runspider .model\Model_NV_so_1.py".split())

def run_NV_1():
    Popen('python .model\Model_NV_so_1.py')





