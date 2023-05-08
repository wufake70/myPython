from appium import webdriver
import time,os
# from selenium.webdriver.common.by import By

info = {
    'platformName':'android',
    'platformVersion':'11.0',
    'deviceName':'192.168.0.69:5555',

    # 'appPackage':'com.tencent.mobileqq',
    # 'appActivity':'.activity.SplashActivity', 
    
          
    'noReset':True,

    'unicodeKeyboard': False,
    'resetKeyboard': False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
x = int(driver.get_window_rect()['width'])/2 
y = int(driver.get_window_rect()['height'])/2

driver.implicitly_wait(3)

# 暂停视频
# driver.find_element_by_id("android:id/tabhost").click()
os.system("adb shell input tap %s %s" % (x/2,y/2))      # 使用 adb 命令

# 点开评论
driver.find_element_by_id("com.tencent.mobileqq:id/o8m").click()
time.sleep(1)

peo_li = []
com_li = []

try:
    for i in range(200): 
        driver.swipe(x,y+700,x,y,300)
        t1 = [i.text for i in driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mobileqq:id/fxo"]')]
        t2 = [i.text for i in driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mobileqq:id/fxm"]')]

        [ peo_li.append(i) if i not in peo_li else "" for i in t1]
        [ com_li.append(i) if i not in com_li else "" for i in t2]
        print("这是第%s 次" % str(i+1))

    
finally:
    with open("./appium/qq小视频评论.txt","w",encoding="utf-8") as fp:
        for i in range(len(peo_li)): 
            fp.write("%s:  %s\n" %(peo_li[i],com_li[i]))

driver.quit()


