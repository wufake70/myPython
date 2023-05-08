from appium import webdriver
import time
# from selenium.webdriver.common.by import By

info = {
    'platformName':'android',
    'platformVersion':'11.0',
    'deviceName':'815c1faf',

    'appPackage':'com.android.settings',
    'appActivity':'.Settings',   
    
          
    'noReset':True,

    'unicodeKeyboard': False,
    'resetKeyboard': False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
x = int(driver.get_window_rect()['width'])/2 
y = int(driver.get_window_rect()['height'])/2

# 获取元素位置 使用 tap方法 进行点击
e = driver.find_element_by_xpath("//*[@text='蓝牙']")
print("x: %s\ny: %s" % (e.location['x'],e.location['y']))
# driver.tap([(e.location['x'],e.location['y'])],200)       # tap方法 是 异步的

# 获取元素 大小
print("height: %s\nwidth: %s" % (e.size["height"],e.size["width"]))














