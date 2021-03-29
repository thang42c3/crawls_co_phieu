from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy import cmdline
import csv
import os
from subprocess import Popen
import logging

req = requests.get('https://www.cophieu68.vn/historyprice.php?currentPage=1&id=pan', verify=False)
soup = BeautifulSoup(req.text, "lxml")

logging.info("OK")
links = soup.find_all('td', {'class': 'td_bottom3 td_bg1'})
print(links[0].text)




