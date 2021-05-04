import schedule
import time
from app.main.service.make_file_csv_service import lich_su_gia_co_phieu


code_co_phieus = ['AAT', 'AAV', 'ABB', 'ABI', 'ABR']

def job():
    for code_co_phieu in code_co_phieus:
        lich_su_gia_co_phieu(code_co_phieu)

schedule.every().day.at("16:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)