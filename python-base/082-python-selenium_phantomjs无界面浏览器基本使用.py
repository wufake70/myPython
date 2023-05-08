# _*_coding :utf-8 _*_
# @Time :2022/5/18 17:18
# @File : 082-python-selenium_phantomjs无界面浏览器基本使用
# @Project : python-base

from selenium import webdriver
path = 'phantomjs.exe'
browser = webdriver.PhantomJS(path)
url = 'https://www.baidu.com/'
browser.get(url)
# 拍照
browser.save_screenshot('002.jpg')































