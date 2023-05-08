# _*_coding :utf-8 _*_
# @Time :2022/5/21 9:25
# @File : 练习008-爬取porn-picture
# @Project : python-base

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://img1.hnllsy.com/pic/4645/5.jpg'
browser.get(url)

# 获取网页源码
page_source = browser.page_source
print(page_source)


























