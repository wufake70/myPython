# _*_coding :utf-8 _*_
# @Time :2022/5/30 14:36
# @File : 练习016
# @Project : python-base

from selenium import webdriver
from lxml import etree
import time
import re

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://i.chaoxing.com/base?t=1653729819330'
browser.get(url)

# 登录学习通
login_username = browser.find_element_by_id('phone')
login_password = browser.find_element_by_id('pwd')
login_button = browser.find_element_by_id('loginBtn')
login_username.send_keys('18794762431')
login_password.send_keys('zxcvbnm70')
login_button.click()
time.sleep(1)  # 成功进入学习通

# 进入指定课程视频的页面（上一步操作，已经校验了referer，可直接使用url打开新页面）
url_my_course = 'https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=457014000&courseId=221546426&clazzid=48311972&enc=e349aa7ae83bed942a6af451034598b4&mooc2=1&cpi=211027122&openc=37273a2e62b36492f8982e8c195cd703'
browser.get(url_my_course)
# 进入章节测试
test = browser.find_element_by_id('dct2')
test.click()
# time.sleep(9)
# 获取下一章节的按钮
next_button = browser.find_element_by_id('right')
next_button = browser.find_element_by_id('right')
# next_button.click() 会报错： element click intercepted（元素点击事件被打断）
# 解决方法如下列代码
# browser.execute_script("arguments[0].click();", next_button)  # execute script 执行脚本
for i_1 in range(115):
    # 进入内联框架
    frame = browser.find_element_by_id('iframe')
    browser.switch_to.frame(frame)
    frame_2 = browser.find_element_by_xpath('//iframe')
    browser.switch_to.frame(frame_2)  # 视频页面
    frame_3 = browser.find_element_by_id('frame_content')
    browser.switch_to.frame(frame_3)  # 章节测试页面

    # 模拟点击视频
    # video_play_button = browser.find_element_by_xpath('//button[@class="vjs-big-play-button"]')
    # print(video_play_button)
    # browser.execute_script("arguments[0].click();", video_play_button)
    # time.sleep(1111)

    # 选择题和判断题
    tree = browser.page_source
    tree = etree.HTML(tree)
    test_content_tm = tree.xpath('//div[@style="width:80%;height:100%;float:left;"]//text()')

    for i in range(len(test_content_tm)):
        print(test_content_tm[i])

    # 退出当前的iframe标签，
    browser.switch_to.default_content()  # 回到主文档

    next_button = browser.find_element_by_id('right')
    browser.execute_script('arguments[0].click();', next_button)
    time.sleep(1)  # 点击事件会被打断，设置时间
    next_button = browser.find_element_by_id('right')   # 每一次点击事件都要重新声明变量，否则会报错：element is not attached to the page document （元素未附加到页面文档）
    browser.execute_script("arguments[0].click();", next_button)
    time.sleep(2)

print('结束')
























