# _*_coding :utf-8 _*_
# @Time :2022/5/28 17:28
# @File : 练习013_-爬取学习通资源
# @Project : python-base

from selenium import webdriver
from lxml import etree
import time

# handless的使用
# from selenium.webdriver.chrome.options import Options
# # headless基本配置
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
# browser = webdriver.Chrome(chrome_options=chrome_options)

path = 'msedgedriver.exe'
browser = webdriver.Edge(path)
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
# 点击播放视频
# video_play_button = browser.find_elements_by_xpath('//button[@class="vjs-big-play-button"]')
# print(video_play_button)
# video_play_button.click()
# 进入章节测试
test = browser.find_element_by_id('dct2')
test.click()
# 获取下一章节的按钮
next_button = browser.find_element_by_id('right')

for i_2 in range(100):
    """
    学习通的iframe（内联框架）有坑
         注意：内敛了三个iframe
    """
    # 切换到iframe标签获取相应数据
    # 一成功进入第一个iframe
    frame = browser.find_element_by_id('iframe')
    browser.switch_to.frame(frame)
    # print(browser.page_source)
    # 第二个iframe（它是视频页面）
    frame_2 = browser.find_element_by_xpath('//iframe')
    browser.switch_to.frame(frame_2)
    # print(browser.page_source)
    # 的三个iframe （章节作业页面）
    frame_3 = browser.find_element_by_id('frame_content')
    browser.switch_to.frame(frame_3)
    # print(browser.page_source)  #  成功进入想到达的页面

    # 模拟点击视频播放
    # video_play_button = browser.find_elements_by_xpath('//button[@class="vjs-big-play-button"]')
    # print(video_play_button)
    # video_play_button.click()

    """
    成功进入内联框架之后，即可后去想要的源码
    """
    # 获取题目
    # 先获取网页源码
    tree = browser.page_source
    # print(tree)
    # 用xpath解析网页源码
    tree = etree.HTML(tree)
    # print(tree)  # 控制台输出 <Element html at 0x1f7fbe977c0>
    test_content_title = tree.xpath('//div[@class="ZyTop"]/h3/text()')
    print(test_content_title[0])
    # 选择题和判断题
    test_content_tm = tree.xpath('//div[@style="width:80%;height:100%;float:left;"]//text()')
    test_content_xz2 = tree.xpath('//div[@class="TiMu"]//form//li//text()')
    # test_content_pd = tree.xpath('')  判断题没有选项直接填入我的答案
    # print(test_content_tm)
    # print(test_content_xz2)
    # 我的答案
    test_content_answer = tree.xpath('//div[@class="Py_answer clearfix"]//span//text()')
    test_content_answer_pd = tree.xpath('//div[@class="Py_answer clearfix"]//span/i/text()')
    for i in range(len(test_content_tm)):

        if '选题' in test_content_tm[i]:  # 区分出选择题
            print(test_content_tm[i])
            print(test_content_xz2[i * 8])
            print(test_content_xz2[i * 8 + 1])
            print(test_content_xz2[i * 8 + 2])
            print(test_content_xz2[i * 8 + 3])
            print(test_content_xz2[i * 8 + 4])
            print(test_content_xz2[i * 8 + 5])
            print(test_content_xz2[i * 8 + 6])
            print(test_content_xz2[i * 8 + 7])
            print(test_content_answer[i])
        # elif '判断题' in test_content_tm[i]:  # 区分出判断题
        #     print(test_content_tm[i])
        #     # print('我的答案：' + test_content_answer_pd[i])

# 点击下一章节
#     next_button.click()
#     time.sleep(0.5)
#     test.click()




