from appium import webdriver
import time,os
# from selenium.webdriver.common.by import By


info = {
    'platformName':'android',
    'platformVersion':'11.0',
    'deviceName':'815c1faf',

    # 'appPackage':'com.chaoxing.mobile',
    # 'appActivity':'.main.ui.MainTabActivity',    
          
    'noReset':True,

    'unicodeKeyboard': False,
    'resetKeyboard': False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
x = int(driver.get_window_rect()['width'])/2 
y = int(driver.get_window_rect()['height'])/2
driver.implicitly_wait(5)

# 获取 全部课程
# course_li = []
# [course_li.append(i.text) for i in driver.find_elements_by_xpath('//*[@resource-id="com.chaoxing.mobile:id/tv_name"]')]

# for i in range(3):
#     last_e = driver.find_elements_by_xpath('//*[@resource-id="com.chaoxing.mobile:id/rl_item"]')[-1]
#     driver.scroll(last_e,driver.find_element_by_xpath("//*[@resource-id='com.chaoxing.mobile:id/toolbar_title_layout']"),2500)
#     ['' if i.text in course_li else course_li.append(i.text) for i in driver.find_elements_by_xpath('//*[@resource-id="com.chaoxing.mobile:id/tv_name"]')]

#     # time.sleep(3)

# print(len(course_li))
# for i in range(len(course_li)): print(course_li[i])


# 课程任务点
# for i in range(16):

#     # 判断任务点 完成情况
#     task_point_li = driver.find_elements_by_xpath("//*[@resource-id='com.chaoxing.mobile:id/tv_icon']")
#     for ii in task_point_li:
#         # 2 没看视频、没做题
#         if ii.text == '2':  
#             driver.tap([(ii.location['x']+100,ii.location['y']+5)],160),print('进入视频界面.....')

#             # 判断 在 播放
#             play_btn = driver.find_element_by_xpath("//*[@text='播放']")
#             if "任务点" in driver.page_source: 
#                 # play_btn.click(),
#                 # driver.tap([(play_btn.location['x']+50,play_btn.location['y']+50)],200)
#                 time.sleep(0.5)
#                 os.system("adb shell input tap %s %s" %(play_btn.location['x']+50,play_btn.location['y']+50))

#                 # 获取大概时间
#                 time.sleep(4)
#                 s_time = driver.find_element_by_id("com.chaoxing.mobile:id/land_total_time").text
#                 e_time = driver.find_element_by_id("com.chaoxing.mobile:id/land_total_time").text
#                 print(s_time,e_time)
#                 print('play video......'),time.sleep(100)
            
      # 滑动
#     last_e = driver.find_elements_by_xpath('//*[@resource-id="com.chaoxing.mobile:id/tv_title"]')[-1]
#     driver.scroll(last_e,driver.find_element_by_xpath("//*[@resource-id='com.chaoxing.mobile:id/title_container']"),3000)


#     if "已经到底了" in driver.page_source: break
    
play_btn = driver.find_element_by_xpath("//*[@text='播放']")
# driver.tap([(play_btn.location['x']+50,play_btn.location['y']+50)],1)
os.system("adb shell input tap %s %s" %(play_btn.location['x']+50,play_btn.location['y']+50))




