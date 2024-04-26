# 定位网页元素
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://ditu.baidu.com/'
service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(service=service, options=opt)
browser.maximize_window()
browser.get(url)
time.sleep(3)

btn = browser.find_element(by=By.XPATH, value='//*[@id="ui3_city_change"]/a')
btn.click()
time.sleep(3)
city_element = browser.find_element(by=By.CSS_SELECTOR, value='#selCityHotCityId > a:nth-child(3)')
city_element.click()
time.sleep(3)
# search_element = browser.find_element(by=By.ID, value='sole-input')
search_element = browser.find_element(by=By.CLASS_NAME, value="searchbox-content-common")
search_element.send_keys('上海交通大学', Keys.ENTER)
time.sleep(3)

browser.quit()

