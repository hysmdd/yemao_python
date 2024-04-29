# 模拟登录豆瓣-过滑块验证
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import uniform
from random import randint

from 夜猫编程.utils.CalculateDistance import CalculateDistance


pyautogui.FAILSAFE = False

def press_button(pic_address, button):
    loc = pyautogui.locateOnScreen(image=pic_address, confidence=0.8)
    p = pyautogui.center(loc)
    pyautogui.moveTo(p)
    time.sleep(1)
    if button == 'right':
        pyautogui.rightClick()
    else:
        pyautogui.leftClick()


def handle_distance(distance):
    # 将直线距离转为缓慢的轨迹
    import random
    slow_distance = []
    while sum(slow_distance) <= distance:
        slow_distance.append(random.randint(-2, 15))

    if sum(slow_distance) != distance:
        slow_distance.append(distance - sum(slow_distance))
    return slow_distance


def drag_slide(tracks, slide_addr):
    # 拖动滑块
    loc = pyautogui.locateOnScreen(slide_addr, confidence=0.9)
    p1 = pyautogui.center(loc)
    print(p1)
    pyautogui.moveTo(p1)
    pyautogui.mouseDown()
    for track in tracks:
        pyautogui.move(track, uniform(-2, 2), duration=0.15)
    pyautogui.mouseUp()


def login(url, user_name, password, path):
    service = Service(executable_path=r"D:\Software\chromedriver-win64\chromedriver.exe")
    opt = Options()
    opt.debugger_address = "127.0.0.1:8888"
    browser = webdriver.Chrome(service=service, options=opt)
    browser.get(url)
    browser.implicitly_wait(5)

    # 点击密码登录
    iframe = browser.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
    browser.switch_to.frame(iframe)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]').click()
    time.sleep(uniform(1, 4))

    # 输入账号
    browser.find_element(By.XPATH, '//*[@id="username"]').send_keys(user_name)
    time.sleep(uniform(1, 4))
    # 输入密码
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(uniform(1, 4))
    # 点击登录
    press_button(r'./images/douban_login_button.png', 'left')
    # browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
    # time.sleep(uniform(1, 4))

    # 进入验证码iframe
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.ID, 'tcaptcha_iframe_dy')))
    code_frame = browser.find_element(By.ID, 'tcaptcha_iframe_dy')
    browser.switch_to.frame(code_frame)

    # 获取滑块背景图片
    background_element = browser.find_element(By.ID, 'slideBg')
    background_location = background_element.location
    print(background_location)

    background_image = background_element.screenshot_as_png
    file_name = time.time()
    with open(fr'{path}/BG-{file_name}.png', 'wb') as f:
        f.write(background_image)
        print('已下载背景图片')

    # 获取滑块图片
    slide_element1 = browser.find_element(By.XPATH, '//*[@id="tcOperation"]/div[7]')
    slide_element2 = browser.find_element(By.XPATH, '//*[@id="tcOperation"]/div[8]')
    s1 = slide_element1.size
    s2 = slide_element2.size
    if s1['width'] > 200 and s1['height'] < 20:
        slide_element = slide_element2
    else:
        slide_element = slide_element1

    slide_location = slide_element.location
    print(slide_location)
    slide_image = slide_element.screenshot_as_png
    with open(fr'{path}/SD-{file_name}.png', 'wb') as f:
        f.write(slide_image)
        print("已下载滑块图片")

    # 背景图片地址和滑块图片的地址
    bg_addr = f'{path}/BG-{file_name}.png'
    sd_addr = f'{path}/SD-{file_name}.png'

    # 计算滑块和背景图片之间x轴距离
    offset_x = slide_location['x'] - background_location['x']
    offset_y = slide_location['y'] - background_location['y']

    slide_offset = CalculateDistance(bg_addr, sd_addr, offset_x, offset_y, True)
    slide_distance = slide_offset.run()

    print(slide_distance)

    # 计算滑块轨迹
    tracks = handle_distance(slide_distance)

    # 拖动滑块
    slide_img_addr = r'./images/douban_slide.png'
    drag_slide(tracks, slide_img_addr)



if __name__ == '__main__':
    url = "https://www.douban.com"
    user_name = "admin@douban.com"
    password = "admin123"
    login(url, user_name, password, r'./images/slide')
