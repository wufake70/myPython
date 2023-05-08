# _*_coding :utf-8 _*_
# @Time :2022/5/29 10:05
# @File : 练习015
# @Project : python-base

from selenium import webdriver

path = 'chromedriver.exe'
driver = webdriver.Chrome(path)
url = "http://okjx.cc/?url=https://v.qq.com/x/cover/m441e3rjq9kwpsc/w0040odz67k.html"
driver.get(url)
iframes = driver.find_elements_by_xpath('//*[@id="divMainJobDescription"]')
print(len(iframes))
# driver.switch_to_frame(iframes)
driver.switch_to(iframes)
print(driver.page_source)























