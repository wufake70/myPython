# _*_coding :utf-8 _*_
# @Time :2022/5/18 12:57
# @File : 080-selenium访问元素信息以及交互


from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com/'
browser.get(url)

# 获取元素信息
# 获取元素的属性
input = browser.find_element_by_id('su')
# print(input.get_attribute('class'))
# 获取元素标签的名字
print(input.tag_name)
# 获取元素文本
a = browser.find_element_by_link_text('新闻')
print(a.text)































