from appium import webdriver
import time
# from selenium.webdriver.common.by import By


info = {
    'platformName':'android',
    'platformVersion':'11.0',
    'deviceName':'815c1faf',

    # 'appPackage':'com.chaoxing.mobile',
    # 'appActivity':'.group.ui.TopicBodyActivity',    
          
    'noReset':True,

    'unicodeKeyboard': False,
    'resetKeyboard': False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
x = int(driver.get_window_rect()['width'])/2 
y = int(driver.get_window_rect()['height'])/2

people_ls = []
order_ls = []
comment_ls = []

for i in range(60):
    try:
        t1 = driver.find_elements_by_xpath("//*[@resource-id='com.chaoxing.mobile:id/tvAuthor']")
        t2 = driver.find_elements_by_xpath('//*[@resource-id="com.chaoxing.mobile:id/tvReplyContent"]')

        ['' if ii.text in people_ls else people_ls.append(ii.text) for ii in t1]
        ['' if ii.text in comment_ls else comment_ls.append(ii.text) for ii in t2]
    except(e):

        print(e)

    print(i)
    driver.swipe(x,y+500,x,y-500,500)

with open("./appium/学习通评论.txt","w",encoding="utf-8") as fp:
    
    for i in range(len(comment_ls)): fp.write(people_ls[i]+":  "+comment_ls[i]+"\n\n")



