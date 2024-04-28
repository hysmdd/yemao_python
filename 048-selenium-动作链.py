# selenium-动作链
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_experimental_option('detach', True)
url = 'https://www.12306.cn/index/'
service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=opt)
browser.implicitly_wait(3)
browser.maximize_window()
browser.get(url)

# 鼠标悬停在车票上
ticket_element = browser.find_element(by=By.XPATH, value='//*[@id="J-chepiao"]/a')
ActionChains(browser).move_to_element(ticket_element).perform()

# 点击单程进入下一步
one_way_element = browser.find_element(by=By.XPATH, value='//*[@id="megamenu-3"]/div[1]/ul/li[1]/a')
ActionChains(browser).click(one_way_element).perform()

# 输入出发地
time.sleep(1)
source_element = browser.find_element(by=By.XPATH, value='//*[@id="fromStationText"]')
ActionChains(browser)\
    .click(source_element)\
    .pause(1)\
    .send_keys('shanghai')\
    .pause(1)\
    .key_down(Keys.ENTER)\
    .perform()

# 输入目的地
time.sleep(1)
dest_element = browser.find_element(by=By.XPATH, value='//*[@id="toStationText"]')
ActionChains(browser)\
    .click(dest_element)\
    .pause(1)\
    .send_keys('bj')\
    .pause(1)\
    .key_down(Keys.DOWN)\
    .pause(1)\
    .key_down(Keys.DOWN)\
    .key_down(Keys.ENTER)\
    .perform()

# 选择出发日期
time.sleep(1)
date_element = browser.find_element(by=By.XPATH, value='//*[@id="train_date"]')
ActionChains(browser)\
    .click(date_element)\
    .pause(1)\
    .key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
    .pause(1)\
    .send_keys(Keys.DELETE)\
    .pause(1)\
    .send_keys('2024-05-01', Keys.TAB)\
    .perform()

# 勾选高铁
time.sleep(1)
browser.find_element(by=By.XPATH, value='//*[@value="G"]').click()

# 选择发车时间
time.sleep(1)
start_time_element = browser.find_element(By.XPATH, '//*[@id="cc_start_time"]')
Select(start_time_element).select_by_visible_text('12:00--18:00')

# 点击查询
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
