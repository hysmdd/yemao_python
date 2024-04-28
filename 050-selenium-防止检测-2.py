# 防止检测-debugging模式

# 找到Chrome浏览器的安装路径
# C:\Program Files\Google\Chrome\Application

# 在命令行模式下输入下面的命令创建配置一个浏览器
# chrome.exe --remote-debugging-port=8888 --user-data-dir="D:\data\chrome\profiles"

# 在Chrome的快捷方式上点击，选择属性，快捷方式的目标栏后面加空格加上下面命令：
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8888 --user-data-dir="D:\data\chrome\profiles"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.debugger_address = '127.0.0.1:8888'
browser = webdriver.Chrome(service=service, options=opt)
url = 'https://www.douban.com/'
