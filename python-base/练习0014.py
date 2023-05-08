# _*_coding :utf-8 _*_
# @Time :2022/5/29 9:54
# @File : 练习0014
# @Project : python-base

# 1.导入库
from selenium.webdriver import Chrome

url4 = 'http://okjx.cc/?url=https://v.qq.com/x/cover/m441e3rjq9kwpsc/w0040odz67k.html'
# 2.获得驱动
driver = Chrome(executable_path = 'chromedriver.exe')
# 3.1 使用驱动 ,打开网页
driver.get(url4)

# 进入iframe
for i in range(4):
    a = driver.find_element_by_xpath('//iframe[1]')
    print(a)
    driver.switch_to.frame(a)

# 获取链接
s = driver.find_element_by_tag_name('video')
print(s.get_property('src'))
# print(driver.page_source)