# _*_coding :utf-8 _*_
# @Time :2022/5/18 17:28
# @File : 083-python-无界面浏览器之chrome-headless
# @Project : python-base

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# headless基本配置
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path
browser = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.baidu.com/'
browser.get(url)
# 拍照
browser.save_screenshot('file_storage/paizhao.jpg')

# 封装的headless