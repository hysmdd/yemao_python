# selenium的基本使用
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.baidu.com"
url1 = "https://www.jd.com"
service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(service=service, options=opt)
browser.maximize_window()
# browser.set_window_position(1000, 20)
# browser.set_window_size(520, 1314)
browser.get(url)
time.sleep(1)
browser.get(url1)
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.refresh()
time.sleep(1)
page_text = browser.page_source
print(page_text)

# browser.close()
browser.quit()
