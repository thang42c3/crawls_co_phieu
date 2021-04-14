from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy import cmdline
import csv
import os
from subprocess import Popen
import logging
from config import config
import json

config = config()
logging.warning(config["url"]['lich_su_gia_co_phieu'])
logging.warning(config["url"]['tai_san'])
logging.warning(config["file_csv_url"]["lich_su_gia_co_phieu"])

with open(r'{0}'.format(config["file_csv_url"]["lich_su_gia_co_phieu"]), newline='') as f:
    reader = csv.reader(f)
    data1 = list(reader)
print(data1)
f.close()
