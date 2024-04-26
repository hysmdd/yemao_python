# 页面加载策略和等待
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.page_load_strategy = 'none'

url = 'https://movie.douban.com/subject/35196753/reviews'
browser = webdriver.Chrome(service=service, options=opt)
browser.implicitly_wait(5)
browser.maximize_window()
start_time = time.time()
browser.get(url)
end_time = time.time()
print(f"打开页面时间: {end_time - start_time}")

locator = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/span[4]/a')
for i in range(10):
    try:
        WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located(locator))
    except:
        print("未找到指定元素")
        browser.quit()
        exit()
    next_page_btn = browser.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[1]/div[2]/span[4]/a')
    param = next_page_btn.get_attribute('href')
    print(f"下一页url：{param}")
    next_page_btn.click()
    time.sleep(1)

browser.quit()
