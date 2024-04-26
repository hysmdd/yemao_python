import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


url = "http://www.baidu.com"
service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.maximize_window()
browser.get(url)
time.sleep(5)
browser.close()
