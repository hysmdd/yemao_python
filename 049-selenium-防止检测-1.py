# 防止检测
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
opt = Options()

driver = webdriver.Chrome(service=service, options=opt)
driver.maximize_window()

with open(r'D:\Software\chromedriver-win64\stealth.min.js') as f:
    js = f.read()
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': js
})

url = 'https://bot.sannysoft.com'
driver.get(url)

