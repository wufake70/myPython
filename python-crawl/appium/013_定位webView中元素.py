from appium import webdriver
import time
# from selenium.webdriver.common.by import By

info = {
    'platformName':'android',
    # 'platformVersion':'11.0',
    'udid':'192.168.0.39:5668',
    
          
    'noReset':True,

    'unicodeKeyboard': False,
    'resetKeyboard': False
}
# 转到定义
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)

print(driver.contexts)


