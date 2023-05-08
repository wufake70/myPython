# _*_coding :utf-8 _*_
# @Time :2022/5/22 21:35
# @File : 练习011-校园网自动登录
# @Project : python-base

from selenium import webdriver
from lxml import etree
import time

path = 'msedgedriver.exe'
browser = webdriver.Edge(path)
url_1 = 'http://authserver.lzjtu.edu.cn/authserver/login?service=http%3A%2F%2Fwebvpn.lzjtu.edu.cn%2Flogin%3Fcas_login%3Dtrue'
browser.get(url_1)

# 兰州交通大学统一身份认证平台登录页面
username_input = browser.find_element_by_id('username')
password_input= browser.find_element_by_id('password')
login_button = browser.find_element_by_id('login_submit')
username_input.send_keys('20211103104')
password_input.send_keys('zxcvbnm70@A')
login_button.click()

# 教务学生登录入口
# time.sleep(1)
# student_get_in_login = browser.find_element_by_xpath('//div[@class="block-group__item__wrap"]//a')
# student_get_in_login.click()
# time.sleep(3)
# 注意：此时进入新的页面不能再用原来的browser了
"""
注意：教务处学生登录入口需要 校验referer（即兰州交通大学统一身份认证成功登录时的页面），当我们在用selenium成功进入兰州交通大学.....的页面时，
再一次使用browser.get(url),此时的url为教务处学生登录的网址，是可以成功进入的,（即referer校验成功）
"""
url_2 = 'http://webvpn.lzjtu.edu.cn/http/494a553139386968732a235e35546e28283a5c701107a40c3558fec7dbedfc35cf1b75/default2.aspx?wrdrecordvisit=1655443886000'
browser.get(url_2)
student_username = browser.find_element_by_id('txtUserName')
student_password = browser.find_element_by_id('TextBox2')
student_username.send_keys('20211103104')
student_password.send_keys('13765450541love')

# 获取图片验证码
# 注意：这里的img数据是动态的，不会与原页面同步
# img = browser.find_element_by_id('icode').get_attribute('src')
# img_1 = 'http://webvpn.lzjtu.edu.cn/http/77726476706e69737468656265737421e8e240922c35265c64029db9d6502720222896/default2.aspx?wrdrecordvisit=1653229839000' + img
# print(img_1)
# 使用拍照功能
browser.save_screenshot('C:/Users/yui/Desktop/my-python/auto_script/img_code.jpg')
# 记住：url编码会对中文进行编码（对中文不友好）
print('file:///C:/Users/yui/Desktop/my-python/auto_script/img_code.jpg')

# 将保存的图片在浏览器中打开
# url = 'file:///C:/Users/yui/Desktop/my-python/auto_script/img_code.jpg'
# browser.get(url)

img_code = input("请快点输入图片验证码：")
img_code_input = browser.find_element_by_id('txtSecretCode')
student_login_button = browser.find_element_by_id('Button1')
img_code_input.send_keys(img_code)
student_login_button.click()


















