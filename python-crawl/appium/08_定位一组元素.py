"""
一、id class xpath 定位一组元素
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
x = int(driver.get_window_rect()['width'])/2 
y = int(driver.get_window_rect()['height'])/2

# 1.通过 id(resource-id) 定位,获取 当前界面 所有组件的名称
txt_li = []
[txt_li.append(i.text) for i in  driver.find_elements_by_id('android:id/title')]

for i in range(5): 
    driver.swipe(x,y+500,x,y-500,600)
    es = driver.find_elements_by_id('android:id/title')
    for ii in es:
        if not (ii.text in txt_li): txt_li.append(ii.text) 
# 打印
for i in txt_li: print(i)

# driver所获取的 元素对象 只能在当前窗口 页面搜索到 相关属性，一旦 超出当前窗口 就不在获取到，相关文本信息 及时保存


















