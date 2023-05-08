"""
一、id class xpath 定位一个元素
"""


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

# 1.通过 id 定位 搜索框
driver.find_element_by_id("com.android.settings:id/animated_hint_layout").click()

# 2.通过 class 定位 输入框 并输入
# send_keys 不能输入中文
# 解决方法: info 加上 'unicodeKeyboard': False,'resetKeyboard': False
time.sleep(1) # 等待 组件加载
driver.find_element_by_class_name("android.widget.EditText").send_keys("hello world 你好世界 ！！！")
time.sleep(1)

# 3.通过 xpath 定位 返回按钮 并点击
e2 = driver.find_element_by_xpath("//*[@text='取消']")
e2.click()

time.sleep(5)
driver.quit()












