# _*_coding :utf-8 _*_
# @Time :2022/5/18 12:32
# @File : 079-python-selenium元素定位
# @Project : python-base

from selenium import webdriver



path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com/'
browser.get(url)

# 元素定位

# 根据id来查找对象
# botton = browser.find_element_by_id('su')
# print(botton)

# 根据标签的name属性值来获取对象，不是标签名
# botton = browser.find_element_by_name('input')
# print(botton)
# botton = browser.find_element_by_name('wd')
# print(botton)

# 根据xpath语句来获取对象
# botton = browser.find_element_by_xpath('//input[@id="su"]')
# print(botton)

# 根据标签的名字来获取对象
# # 当elements会返回一个列表
# button = browser.find_elements_by_tag_name('input')
# print(button)

# 根据css选择器 (bs4的语法来获取对象)
# button = browser.find_element_by_css_selector('#su')
# print(button)

#
button = browser.find_element_by_link_text('视频')
print(button)






























