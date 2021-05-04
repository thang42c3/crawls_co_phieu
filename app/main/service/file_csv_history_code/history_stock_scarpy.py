import json
import scrapy
from scrapy import cmdline
import csv
import os
from config.config import configs
from app import db

config = configs()
# NHIá»†M Vá»¤ Sá» 1

'''
Mục đích: Là lấy toàn bộ dữ liệu về lịch sử giá cổ phiếu sử dụng scrapy.
'''
'''
# Đoạn mã này với mục đích tập hợp toàn bộ link của toàn bộ khoảng 1.800 mã cổ phiếu. 
# Tuy nhiên do số lượng quá lớn nên tạm thời sẽ không sử dụng đoạn mã này mà chỉ dùng khoảng 5 mã cổ phiếu
ma_co_phieu = ma_co_phieus.query.all()
start_urls1 = []
for ma_co_phieu2 in ma_co_phieu:
    ma_co_phieu1 = ma_co_phieu2.code
    url_csv_file = config["file_csv_url"]["lich_su_gia_co_phieu"] + "-{0}".format(ma_co_phieu1)
    start_urls1.append(config["url"]["lich_su_gia_co_phieu"] + "{0}".format(ma_co_phieu1))
'''


start_urls1 = ['https://www.cophieu68.vn/historyprice.php?id=AAT',
               'https://www.cophieu68.vn/historyprice.php?id=AAV',
               'https://www.cophieu68.vn/historyprice.php?id=ABB',
               'https://www.cophieu68.vn/historyprice.php?id=ABI',
               'https://www.cophieu68.vn/historyprice.php?id=ABR']
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

for star_url in start_urls1:
    page = star_url.split("=")[-1]
    if os.path.exists(r"..\\..\\..\\..\\file_csv\\lich_su_gia_co_phieu_{0}.csv".format(page)):
        os.remove(r"..\\..\\..\\..\\file_csv\\lich_su_gia_co_phieu_{0}.csv".format(page))
    with open(r"..\\..\\..\\..\\file_csv\\lich_su_gia_co_phieu_{0}.csv".format(page), 'a') as f:
        write = csv.writer(f)
        write.writerow(fields)

class CpSpider(scrapy.Spider):
    name = 'cp_item'
    start_urls = start_urls1
    #for i in range(1, 72):
        #   start_urls.append('https://www.cophieu68.vn/historyprice.php?currentPage={0}&id={1}'.format(i, Ten_cty))
    def parse(self, response):
        rows = []
        page = response.url.split("=")[-1]
        for table in response.css('table.stock'):
            for j in range (2, 120):
                record = [ table.xpath('tr[{0}]/td[1]/text()'.format(j)).get(),
                    page,
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
                if record[3] is not None:
                    rows.append(record)
        Page = response.xpath("//ul[@id='navigator']/li[9]/a[1]/@href").get()
        if Page is not None:
            next_page = response.xpath("//ul[@id='navigator']/li[9]/a[1]/@href").get()
        elif response.xpath("//ul[@id='navigator']/li[6]/span[1]/text()").get() == "70":
            next_page = response.xpath("//ul[@id='navigator']/li[7]/a[1]/@href").get()
        elif response.xpath("//ul[@id='navigator']/li[7]/span[1]/text()").get() == "71":
            next_page = None
        else:
            next_page = response.xpath("//ul[@id='navigator']/li[6]/a[1]/@href").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)



        with open(r"..\\..\\..\\..\\file_csv\\lich_su_gia_co_phieu_{0}.csv".format(page), 'a') as f:
            write = csv.writer(f)
            write.writerows(rows)

cmdline.execute("scrapy runspider history_stock_scarpy.py".split())


