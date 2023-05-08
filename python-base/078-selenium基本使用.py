# _*_coding :utf-8 _*_
# @Time :2022/5/16 14:38
# @File : 078-selenium基本使用
# @Project : python-base


# chrome浏览器内核驱动
# https://chromedriver.storage.googleapis.com/index.html

# 导入selenium
from selenium import webdriver

# 创建浏览器操作对象
# 浏览器驱动的文件路径
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网站，请注意：不能挂梯子使用
data = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsMSw2LDUsNCw4LDcsOQ%3D%3D&word=%E6%9D%8E%E6%99%BA%E6%81%A9'

browser.get(data)

# browser.page_source  获取当前也面源码


















