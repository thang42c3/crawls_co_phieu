from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.cophieu68.vn/historyprice.php?id=pan#")
element = driver.find_element_by_link_text("Đăng nhập")
element.click()
time.sleep(5)
user = driver.find_element_by_name("username")
user.send_keys("ducthangbnn@gmail.com")
password = driver.find_element_by_name("tpassword")
password.send_keys("Oivung1215")
driver.find_element_by_xpath("//a[contains(@onclick,'checkFormLogin()')]").click()
time.sleep(3)
element = driver.find_element_by_link_text("Export Excel")
element.click()
