# 切换窗口
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

for i in range(0, 41):
    url = f'https://movie.douban.com/subject/35196753/reviews?start={i*20}'
    service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
    opt = Options()
    opt.page_load_strategy = 'none'
    opt.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Chrome(service=service, options=opt)
    browser.maximize_window()
    browser.get(url)
    time.sleep(3)
    # browser.quit()

    locator = (By.XPATH, '//div[@class="main-bd"]/h2/a')
    WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located(locator))
    next_page = browser.find_elements(by=By.XPATH, value='//div[@class="main-bd"]/h2/a')
    for title in next_page:
        action = ActionChains(browser).key_down(Keys.CONTROL).key_down(Keys.SHIFT)
        action.click(title).perform()
        time.sleep(3)
        browser.switch_to.window(browser.window_handles[-1])

        locator1 = (By.XPATH, '//div[@id="content"]/div/div[1]/h1/span')
        WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located(locator1))
        author = browser.find_element(by=By.XPATH, value='//header[@class="main-hd"]/a[1]/span').text
        publish_time = browser.find_element(by=By.XPATH, value='//div[@class="main-meta"]/span[1]').text
        file_name = browser.find_element(by=By.XPATH, value='//div[@id="content"]/div/div[1]/h1/span').text
        city = browser.find_element(by=By.XPATH, value='//div[@class="main-meta"]/span[2]').text
        content = browser.find_element(by=By.XPATH, value='//div[@class="review-content clearfix"]').text
        pattern = r"[^\w\s]"
        file_name = re.sub(pattern, '', file_name)
        with open(fr'./file/comments/{file_name}.txt', 'w', encoding='utf-8') as f:
            f.write(f"标题：{file_name}" + '\n')
            f.write(f'发布人：{author}\n')
            f.write(f'发布地点：{city}\n')
            f.write(f"发布时间：{publish_time}\n\n")
            f.write(content)
            print(f"{file_name}已下载...")
        browser.close()
        browser.switch_to.window(browser.window_handles[0])


