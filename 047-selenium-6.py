# 模拟豆瓣登录
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://www.douban.com/'
service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(service=service, options=opt)
browser.maximize_window()
browser.implicitly_wait(5)
browser.get(url)

time.sleep(3)
iframe = browser.find_element(by=By.XPATH, value='//*[@id="anony-reg-new"]/div/div[1]/iframe')
browser.switch_to.frame(iframe)
browser.find_element(by=By.XPATH, value='//div[@class="account-body-tabs"]/ul[1]/li[2]').click()
time.sleep(3)
browser.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys('18512345678')
time.sleep(3)
browser.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('admin123')
time.sleep(3)
browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
time.sleep(3)

browser.switch_to.default_content()
browser.close()
