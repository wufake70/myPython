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

e = driver.find_element_by_xpath("//*[contains(@text,'W')]")
# 使用 get_attribute(属性名)
print(e.get_attribute("enabled"))
print(e.get_attribute("resourceId"))
print(e.get_attribute("className"))
print(e.get_attribute("name"))          # content-desc




















