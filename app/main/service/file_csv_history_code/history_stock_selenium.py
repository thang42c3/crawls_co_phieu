from selenium import webdriver
import time
from config.config import configs
from app.forms import ma_co_phieus

'''
Đầu vào: Dữ liệu các mã cổ phiếu.
Đầu ra: Các file excell được download trực tiếp từ website ứng với từng mã"
'''
config = configs()
ma_co_phieu = ma_co_phieus.query.all()
driver = webdriver.Chrome()
driver.get("https://www.cophieu68.vn")
element = driver.find_element_by_link_text("Đăng nhập")
element.click()
time.sleep(3)
user = driver.find_element_by_name("username")
user.send_keys("ducthangbnn@gmail.com")
password = driver.find_element_by_name("tpassword")
password.send_keys("Oivung1215")
driver.find_element_by_xpath("//a[contains(@onclick,'checkFormLogin()')]").click()
time.sleep(3)


def lich_su_gia_co_phieu(ma_co_phieu1):
  driver.get("https://www.cophieu68.vn/historyprice.php?id={0}#".format(ma_co_phieu1))
  time.sleep(3)
  element = driver.find_element_by_link_text("Export Excel")
  element.click()


for ma_co_phieu2 in ma_co_phieu:
    lich_su_gia_co_phieu(ma_co_phieu2.code)


