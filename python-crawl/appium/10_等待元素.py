"""
一、元素等待
    1.由于一些原因，某些元素并没有立刻出来，此时直接定位会报错。
        网络原因、手机配置原因
"""

from appium import webdriver
import time
# from selenium.webdriver.common.by import By


info = {
    'platformName':'android',
    'platformVersion':'11.0',
    'deviceName':'815c1faf',

    'appPackage':'com.chaoxing.mobile',
    'appActivity':'.main.ui.MainTabActivity',   
    
          
    'noReset':True,

    'unicodeKeyboard': False,
    'resetKeyboard': False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
x = int(driver.get_window_rect()['width'])/2 
y = int(driver.get_window_rect()['height'])/2


# 隐式等待: 指定等待元素(针对全部元素)加载的时长，超出 抛出 NoSuchElementException异常
# driver.implicitly_wait(4)
# e = driver.find_element_by_xpath('//*[@text="课程"]')
# print(e.text)


# 显式等待: 指定等待元素(针对单个元素)加载的时长，超出 抛出 NoSuchElementException异常
from selenium.webdriver.support.wait import WebDriverWait
# 创建 对象
wait = WebDriverWait(driver,5,0.1)      # 传入 driver对象、等待时间、轮询时间
e = wait.until(lambda x: x.find_element_by_xpath('//*[@text="课程"]'))
print(e.text)
















