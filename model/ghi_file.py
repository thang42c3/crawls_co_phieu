import os
import requests
import json
import csv
import os

def ghi_file(url_csv_file, rows):
    if os.path.exists(r'{0}'.format(url_csv_file)):
        os.remove(r'{0}'.format(url_csv_file))

    with open(r'{0}'.format(url_csv_file), 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(rows)
